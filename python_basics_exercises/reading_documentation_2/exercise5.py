# The Python documentation for the datetime module provides two attributes to
# retrieve the year from a date or datetime object: year and isocalendar

from datetime import date # Imports date class from datetime module

today = date.today() # Method returning current date

today_year = today.year # Returns year attribute from date object

iso_year = today.isocalendar()[0] # Returns year element from tuple

# What is the difference between the year attribute
# and the isocalendar method?

# The year attribute returns the year attribute from a given date object
# without creating a new object

# The .isocalendar method returns a tuple object with year, week, and weekday.
# We can then return an element using indexes

# An ISO year starts with a week which has at least 4 days in new year
