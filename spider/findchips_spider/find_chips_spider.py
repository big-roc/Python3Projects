# coding:utf8
import json
import re
import requests
from lxml import etree


def parse_img(td):
    """
    过滤错误的图片
    """
    if td is None:
        return None
    elif td:
        if td[0].strip().endswith('png'):
            return None
        return td[0].strip()


def get_content_from_url(url):
    """
    根据URL获取响应内容
    :param url: 请求的URL
    :return: URL响应的内容字符串
    """
    response = requests.get(url)
    return response.content.decode()


def parse_form_head(html):
    """
    解析HTML, 获取head
    """
    form_head_list = []
    etree_html = etree.HTML(html)
    form_head = etree_html.xpath('//thead/tr[2]/th')
    i = 1
    for head in form_head:
        if head.text is None:
            form_head_list.append('form_head_param_' + str(i))
            i += 1
        else:
            form_head_list.append(head.text.strip())
    return form_head_list


def parse_form_body(html):
    """
    解析HTML, 获取body
    """
    etree_html = etree.HTML(html)
    form_body_list = etree_html.xpath('//table[@id="j-parametric-table"]/tbody/tr')
    return form_body_list


def url_list_joint(model, nums):
    """
    拼接URL列表
    """
    url_lists = []
    n = nums // 20 + 1
    for i in range(1, n + 1):
        model_url = 'http://www.findchips.com/parametric/Diodes/Rectifier%20Diodes?' \
                    'term={}&Manufacturer%20Part%20Number={}&sort=Risk%20Rank%20asc&page={}'.format(model, model, i)
        url_lists.append(model_url)
    return url_lists


def form_head_list_transfer(form_head_list):
    """
    list转换成dict
    """
    form_head_dict = {}
    for i, form_head in enumerate(form_head_list):
        form_head_dict[form_head] = i + 1
    return form_head_dict


def xpath_str_joint(form_head_dict):
    """
    拼接xpath
    """
    form_head_all_xpath_dict = {'form_head_param_1': './td[*]/input/@type',
                                'form_head_param_2': './td[*]/div/img/@src',
                                'form_head_param_3': './td[*]/a[1]/@href',
                                'Composite Price': './td[*]/a[1]/text()',
                                'Samacsys Description': './td[*]//span/text()'}
    form_head_null = ['Risk Rank', 'Pbfree Code', 'Rohs Code']
    form_head_xpath = {}
    for form_head, column_num in form_head_dict.items():
        if form_head in form_head_all_xpath_dict:
            xpath_str = form_head_all_xpath_dict[form_head].replace('*', str(column_num))
            form_head_xpath[form_head] = xpath_str
        elif form_head == 'Part Number':
            list_1 = './td[*]/a[1]/div/text()'.replace('*', str(column_num))
            list_2 = './td[3]/span[1]/text()'.replace('*', str(column_num))
            form_head_xpath[form_head] = [list_1, list_2]
        elif form_head in form_head_null:
            form_head_xpath[form_head] = None
        else:
            xpath_str = './td[%d]/text()' % column_num
            form_head_xpath[form_head] = xpath_str
    return form_head_xpath


def xpath_extract(form_body_list, form_head_xpath):
    """
    通过xpath, 提取数据
    """
    res_list = []
    for tr in form_body_list:
        try:
            row_dict = {}
            for form_head, xpath_str in form_head_xpath.items():
                if xpath_str is None:
                    # print('样式数据, 取不到！')
                    continue
                elif form_head == 'Part Number':
                    td = tr.xpath(form_head_xpath[form_head][0])[0].strip() + ' ' + \
                         tr.xpath(form_head_xpath[form_head][1])[0].strip()
                    if td:
                        row_dict[form_head] = td
                    else:
                        row_dict[form_head] = ''
                elif form_head == 'form_head_param_3':
                    td = tr.xpath(form_head_xpath[form_head])
                    if td:
                        td = parse_img(td)
                        row_dict[form_head] = td
                    else:
                        row_dict[form_head] = ''
                elif form_head == 'Samacsys Description':
                    td = tr.xpath(xpath_str)
                    if td:
                        row_dict[form_head] = ''.join(td)
                    else:
                        row_dict[form_head] = ''
                else:
                    td = tr.xpath(xpath_str)
                    if td:
                        row_dict[form_head] = re.sub(r'[ \r\n]', '', td[0].strip())
                    else:
                        row_dict[form_head] = ''
            form_body_dict = {tr.get('data-part'): row_dict}
            res_list.append(form_body_dict)
        except ValueError as e:
            print('xpath路径错误')
    return res_list


def load_params(res_json):
    """
    json数据写入文件
    """
    with open('find_chips.json', mode='w', encoding='utf-8') as fp:
        json.dump(res_json, fp)


def run(url):
    # 1.获取html
    html = get_content_from_url(url)
    # 2.解析表头
    form_head_list = parse_form_head(html)
    # print(form_head_list)
    # 3.解析body
    form_body_list = parse_form_body(html)
    # print(form_body_list)

    # 4.提取body字段
    form_head_dict = form_head_list_transfer(form_head_list)
    # print(form_head_dict)
    form_head_xpath = xpath_str_joint(form_head_dict)
    res_list = xpath_extract(form_body_list, form_head_xpath)
    return res_list


def start_requests(model, nums):
    """
    循环发送请求
    """
    url_lists = url_list_joint(model, nums)

    find_chips = []
    for url in url_lists:
        res_list = run(url)
        find_chips = find_chips + res_list

    # 转成json
    res_json = json.dumps(find_chips, ensure_ascii=False)
    print(res_json)

    # 5.保存数据
    load_params(res_json)


def get_nums(html):
    """
    解析HTML,获取总条数
    """
    etree_html = etree.HTML(html)
    nums = etree_html.xpath('//*[@id="page"]/div[1]/div[2]/p/strong[2]/text()')[0]
    return int(nums)


def main():
    model_list = ['bav99']
    for model in model_list:
        model_url = 'http://www.findchips.com/parametric/Diodes/Rectifier%20Diodes?' \
                    'term={}&Manufacturer%20Part%20Number={}&sort=Risk%20Rank%20asc&page=1'.format(model, model)
        html = get_content_from_url(model_url)
        nums = get_nums(html)
        start_requests(model, nums)


if __name__ == '__main__':
    main()
