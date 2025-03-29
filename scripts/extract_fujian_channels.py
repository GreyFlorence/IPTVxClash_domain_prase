import requests

LIVE_URL = "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/live.txt"

def extract_fujian_channels():
    """从 live.txt 提取福建频道的内容"""
    response = requests.get(LIVE_URL)
    response.raise_for_status()  # 如果请求失败，抛出异常

    content = response.text
    start_marker = "☘️福建频道,#genre#"
    end_marker = "☘️甘肃频道,#genre#"

    # 查找标记位置
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index == -1 or end_index == -1:
        print("无法找到指定的福建频道区域")
        return

    # 提取内容
    fujian_content = content[start_index:end_index].strip()

    # 将结果写入 fujian_iptv.txt
    with open("fujian_iptv.txt", "w", encoding="utf-8") as f:
        f.write(fujian_content)

    print("已提取福建频道并保存到 fujian_iptv.txt")

if __name__ == "__main__":
    extract_fujian_channels()
