import requests
import yaml
import re

# M3U 直播源列表（修改为你的源）
M3U_URLS = [
    "https://example.com/source1.m3u",
    "https://example.com/source2.m3u"
]

DOMAIN_PATTERN = re.compile(r'https?://([^:/]+)')

def extract_domains(m3u_urls):
    """ 从多个 M3U 文件提取域名并去重 """
    domains = set()

    for url in m3u_urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            domains.update(DOMAIN_PATTERN.findall(response.text))
        except requests.RequestException as e:
            print(f"无法获取 {url}: {e}")

    return sorted(domains)

def update_yaml(domains):
    """ 更新 domains.yml 文件 """
    data = {"payload": domains}

    with open("domains.yml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

def main():
    domains = extract_domains(M3U_URLS)
    update_yaml(domains)

if __name__ == "__main__":
    main()
