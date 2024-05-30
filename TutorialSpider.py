# Welcome! 
# This spider is designed to scrape any given fandom tag on Archive of Our Own. It will scrape the date, word count, tags, and category of each work. The spider will then follow the next page link and scrape the same information from the next page. The spider will continue to follow the next page link until there are no more pages to scrape.
# Before you begin, make sure you have used the 'scrapy startproject [PROJECT NAME]' command in the terminal to create a new project and the 'scrapy genspider [SPIDER NAME] [DOMAIN NAME]' command to create a new spider. Note that the domain name should only read "archiveofourown.org" without https://, www, or any specific fandom tag, we'll add that later.
# This is a general instruction file, so you'll need to fill in the bracketed blanks with the appropriate information.
# Remember to delete both the brackets and the # symbol after you're done, but make sure to leave the quotation marks.
# First go to settings.py and change the ROBOTSTXT_OBEY to False. This will allow the spider to scrape the website.
# Next, set the user agent to a unique name. This will help the website identify the spider and prevent it from being blocked. It's polite to use your email address as the user agent.
# Then, set the download delay to 3. This will prevent the spider from overwhelming the website with requests.
# Now, go to the spider file and fill in the bracketed blanks with the appropriate information. The spider will scrape the website based on the information you provide. This might take some doing, but there is plenty of help to be had in either Youtube tutorials or the forums at StackOverflow.
# To begin, open the terminal (either in Visual Studio Code or another terminal such as Windows Powershell) by pressing ctrl+ö or in the menu under "View" and navigate to the folder where the spider is saved. Type "scrapy crawl [SPIDERNAME HERE] -o [OUTPUT FILE NAME].json" and press enter. The spider will begin to scrape the website and save the information to the output file.
# Good luck and happy scraping!

import scrapy


#class [SPIDERNAME HERE]Spider(scrapy.Spider):
    #name = "[SPIDERNAME HERE]"
    allowed_domains = ["archiveofourown.org"]
    #start_urls = ["[FANDOM TAG URL HERE]"]

    def parse(self, response):
        works = response.css('li[class^="work blurb group"]')
        for work in works:
            yield {
                 # This list tells the spider what information to scrape from the website. You can add or remove information as needed, but for that you'll need to use the 'inspect' or 'developer tool' functions in your browser.
                 # Make note of the ".get" and ".getall" expressions, which are used to scrape the information. ".get" is used for single items, while ".getall" is used for multiple items.
                'date' : work.css('p::text').get(),
                'word' : work.css('dd::text').getall(),
                'tags' : work.css('li a::text').getall(),
                'category' : work.css('li span::text').getall()
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
                if 'https://archiveofourown.org' in next_page:
                    #next_page_url = '[FANDOM TAG ENDING IN /works]' + next_page
                else: 
                    #next_page_url = '[FANDOM TAG ENDING IN /works? YES, WITH THE QUESTION MARK AND EVERYTHING]' + next_page
                yield response.follow(next_page_url, callback=self.parse)
