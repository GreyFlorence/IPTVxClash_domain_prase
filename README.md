# M3U Domain and IP Extractor

![GitHub Actions Status](https://github.com/yourusername/repo-name/workflows/M3U%20Domain%20and%20IP%20Extractor/badge.svg)

A GitHub Actions-powered tool that automatically extracts domains and IP addresses from M3U live stream sources and generates separate YAML files for each.

## 🌟 Features

- **Automated Extraction**: Daily updates via GitHub Actions
- **Clean Separation**: Domains and IPs are stored in separate files
- **Format Verification**: Ensures only valid domains and IPs are included
- **YAML Output**: Generates properly formatted YAML files
- **Manual Trigger**: Run the workflow on-demand when needed

## 📋 Output Files

The workflow produces two YAML files:

### domains.yml
```yaml
payload:
  - 'example.com'
  - 'stream.service.com'
  - 'live.broadcast.net'
```

### ips.yml
```yaml
payload:
  - '192.168.1.1'
  - '10.0.0.1'
  - '172.16.0.5'
```

## 🚀 Setup

1. **Fork or clone this repository**

2. **Configure your M3U sources**:
   - Edit `.github/scripts/extract_domains_ips.py`
   - Update the `M3U_SOURCES` list with your source URLs:
     ```python
     M3U_SOURCES = [
         "https://example.com/playlist.m3u",
         "https://anothersite.com/live.m3u",
         # Add more sources as needed
     ]
     ```

3. **Set up GitHub Actions**:
   - The workflow is already configured to run daily
   - No additional setup is needed

4. **Run manually (optional)**:
   - Go to your repository on GitHub
   - Navigate to Actions → M3U Domain and IP Extractor
   - Click "Run workflow"

## ⚙️ How It Works

1. The GitHub Action runs on the configured schedule (daily by default)
2. Python script fetches M3U content from the specified sources
3. Regular expressions extract URLs and separate domains from IP addresses
4. Results are formatted into YAML and saved to `domains.yml` and `ips.yml`
5. Changes are automatically committed and pushed to the repository

## 🔧 Customization

### Changing the Schedule

Edit `.github/workflows/m3u-extractor.yml` and modify the `cron` value:

```yaml
schedule:
  - cron: '0 0 * * *'  # Default: Run daily at midnight UTC
```

Examples:
- `'0 */6 * * *'`: Every 6 hours
- `'0 0 * * 1'`: Weekly on Monday at midnight UTC
- `'0 0 1 * *'`: Monthly on the 1st at midnight UTC

### Adding Filtering Rules

To add custom filtering for domains or IPs, modify the validation functions in the Python script.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
