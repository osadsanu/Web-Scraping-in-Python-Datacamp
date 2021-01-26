# Create an xpath to the href attributes
xpath = '//a[contains(@attr,"string")]/@href'

# Print out how many elements are selected
how_many_elements( xpath )
# Preview the selected elements
preview( xpath )
