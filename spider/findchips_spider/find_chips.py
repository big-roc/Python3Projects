# coding:utf8
import re
import requests
from lxml import etree
import pandas as pd


def parse_img(td):
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


def parse_form_body(html, form_head_list):
    """
    解析HTML, 获取body
    """
    form_body_list = []
    etree_html = etree.HTML(html)
    form_body = etree_html.xpath('//table[@id="j-parametric-table"]/tbody/tr')
    for tr in form_body:
        try:
            td_1 = tr.xpath('./td[1]/input/@type')
            td_2 = tr.xpath('./td[2]/div/img/@src')
            td_2 = parse_img(td_2)
            td_3 = tr.xpath('./td[3]/a[1]/div/text()')[0].strip() + ' ' + tr.xpath('./td[3]/span[1]/text()')[
                0].strip()
            td_4 = tr.xpath('./td[4]/a[1]/@href')
            td_5 = tr.xpath('./td[5]/a[1]/text()')
            td_9 = tr.xpath('./td[9]/text()')
            td_49 = tr.xpath('./td[49]//span/text()')
            print(len(form_head_list))
            print(len(td_49))
            row_dict = {form_head_list[0]: td_1[0].strip() if td_1 else None,
                        form_head_list[1]: td_2,
                        form_head_list[2]: td_3,
                        form_head_list[3]: td_4[0].strip() if td_4 else None,
                        form_head_list[4]: td_5[0].strip() if td_5 else None,
                        form_head_list[5]: None,
                        form_head_list[6]: None,
                        form_head_list[7]: None,
                        form_head_list[8]: td_9[0].strip() if td_9 else None,
                        form_head_list[48]: ''.join(td_49) if td_49 else None}
            for i, td in enumerate(tr.getchildren()):
                if 9 < i < 49:
                    row_dict[form_head_list[i - 1]] = re.sub(r'[ |\r|\n]', '', tr.xpath('./td[%d]/text()' % i)[0])
            form_body_dict = {tr.get('data-part'): row_dict}
            print(form_body_dict)
            form_body_list.append(form_body_dict)
        except ValueError as e:
            print('xpath路径错误')
    return form_body_list


def load_params(form_body_list):
    """
    数据入库
    """
    df = pd.DataFrame(form_body_list)
    df.to_csv('./find_chips.txt', mode='a', header=None, index=None, encoding='utf8')


def run(url):
    # 1.获取html
    html = get_content_from_url(url)
    # 2.解析表头
    form_head_list = parse_form_head(html)
    # 2.解析body
    form_body_list = parse_form_body(html, form_head_list)
    # 3.保存数据
    load_params(form_body_list)


def start_requests(model, nums):
    url_lists = []
    n = nums // 20 + 1
    for i in range(1, 2):
        model_url = 'http://www.findchips.com/parametric/Diodes/Rectifier%20Diodes?' \
                    'term={}&Manufacturer%20Part%20Number={}&sort=Risk%20Rank%20asc&page={}'.format(model, model, i)
        url_lists.append(model_url)

    for url in url_lists:
        run(url)


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
