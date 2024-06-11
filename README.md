# Web Scraping Tool for News Headlines

This repository contains a Python script `scraper.py` for fetching and displaying news headlines from a specified website using BeautifulSoup and requests libraries.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Pranjol-Dev/web-scraping-tool.git
   cd web-scraping-tool
   ```

2. Install dependencies:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Modify the URL in `scraper.py` with the website you want to scrape headlines from.

4. Run the script:

   ```bash
   python scraper.py
   ```

5. The script will fetch and display news headlines from the specified website.

## Example

For scraping news headlines from the BBC News website, modify `scraper.py`:

```python
url = 'https://www.bbc.com/news'
```

## Dependencies

- Python 3.6 or higher
- `requests` library for making HTTP requests
- `beautifulsoup4` library for parsing HTML

## Notes

- Ensure responsible use of web scraping techniques and comply with the target website's terms of service.
- Customize the script for different websites and data extraction needs as required.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

- GitHub: [Pranjol-Dev](https://github.com/Pranjol-Dev)
