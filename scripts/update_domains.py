import requests
import yaml
import re

# M3U 直播源列表（修改为你的源）
M3U_URLS = [
  "https://raw.githubusercontent.com/YueChan/Live/main/Global.m3u"
]

DOMAIN_PATTERN = re.compile(r'https?://([^:/]+)')
IP_PATTERN = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

def extract_domains_and_ips(m3u_urls):
    """ 从多个 M3U 文件提取域名和 IP 并去重 """
    domains = set()
    ips = set()

    for url in m3u_urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # 提取域名和IP
            domains.update(DOMAIN_PATTERN.findall(response.text))
            ips.update(IP_PATTERN.findall(response.text))

        except requests.RequestException as e:
            print(f"无法获取 {url}: {e}")

    return sorted(domains), sorted(ips)

def update_yaml(domains, ips):
    """ 更新 domains.yml 和 ips.yml 文件 """
    # 写入域名
    with open("domains.yml", "w", encoding="utf-8") as f:
        yaml.dump({"payload": domains}, f, allow_unicode=True, default_flow_style=False)

    # 写入 IP 地址
    with open("ips.yml", "w", encoding="utf-8") as f:
        yaml.dump({"payload": ips}, f, allow_unicode=True, default_flow_style=False)

def main():
    domains, ips = extract_domains_and_ips(M3U_URLS)
    update_yaml(domains, ips)

if __name__ == "__main__":
    main()
