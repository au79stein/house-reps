# scrape house of representatives to get a list of all members of congress

## Challenges

I don't do this often enough.  I don't know if this is a feature, a bug, or just something that some web dev tool does.

Anyway, if you look at the website, it lists all the members of the house of representatives.  
There are two 'tabs' - one tab lists the house members grouped by their state.  
The other tab lists house members, alphabetically by last name.  
This is the one I wanted.

But, looking at the html and the layout of this page, 
each state is it's own table.  Just like each starting letter for a last name is it's own table.

This presents challenges scraping.  If you want the list of members by last name, you need to skip over all the tables that are by state and district.
You can scrape across tables if you can limit yourself to the set of tables that are associated with first letter of last name only.

Anyway, I will embellish more later... 

## How to resolve

the quick answer is to use goquery.  
Goquery allows you to select web page elements like jquery, pretty much using the same syntax...

You need to be a little creative but you can then scrape across tables to generate the list of representatives.


