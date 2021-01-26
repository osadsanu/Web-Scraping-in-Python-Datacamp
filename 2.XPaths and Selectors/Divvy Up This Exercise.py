from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector( text = html )

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )


#Referring to the divs variable you created in the previous exercise, choose the incorrect response.
"""The code len( divs[2].xpath('./*') ) gives the total number of children of the third div element in the HTML code."""
