from bs4 import BeautifulSoup as Soup 
from Draft import create_draft
import pandas as pd

def create_html_content( email, score, impact, brevity, style, sections, texts ):
	html =""

	with open("base_file.html", "r") as base_html:
		html = base_html.read()

	soup = Soup( html, features="html.parser" )


	# setting overall score
	div = soup.find_all("div", {"class": "overall-score"})
	div[0].string = "Resume Score: " + str( score )

	# setting impact
	pie_for_impact = soup.find_all("div", {"class": "pie-for-impact"} )
	new_div = soup.new_tag("div class='pie animate' style='--p:"  + str(impact) + ";--c:orange;font-size:20px;font-weight:bold'")
	new_div.string = str( impact ) + "%"
	pie_for_impact[0].insert_after( new_div )

	div = soup.find_all("span", {"class": "impact-percentage-span"})
	# div[0].string = str( impact ) + "%"


	# setting brevity 
	pie_for_impact = soup.find_all("div", {"class": "pie-for-brevity"} )
	new_div = soup.new_tag("div class='pie animate' style='--p:"  + str(brevity) + ";--c:lightgreen;font-size:20px;font-weight:bold'")
	new_div.string = str( brevity ) + "%"
	pie_for_impact[0].insert_after( new_div )

	div = soup.find_all("span", {"class": "brevity-percentage-span"})
	# div[0].string = str( brevity ) + "%"

	# setting style 
	pie_for_impact = soup.find_all("div", {"class": "pie-for-style"} )
	new_div = soup.new_tag("div class='pie animate' style='--p:"  + str(style) + ";--c:purple;font-size:20px;font-weight:bold'")
	new_div.string = str( style ) + "%"
	pie_for_impact[0].insert_after( new_div )

	div = soup.find_all("span", {"class": "style-percentage-span"})
	# div[0].string = str( style ) + "%"

	# setting sections
	pie_for_impact = soup.find_all("div", {"class": "pie-for-sections"} )
	new_div = soup.new_tag("div class='pie animate' style='--p:"  + str(sections) + ";font-size:20px;font-weight:bold'")
	new_div.string = str( sections ) + "%"
	pie_for_impact[0].insert_after( new_div )

	div = soup.find_all("span", {"class": "sections-percentage-span"})
	# div[0].string = str( sections ) + "%"
	
	# setting suggestions section
	suggestion_list = soup.select("table.table-1-heading")
	headings = [ "Impact", "Brevity", "Style", "Section" ]

	for i, suggestions in enumerate( suggestion_list ): 
		rows = suggestions.find_all("tr")
		for row in rows: 
			strong = row.find_all( "strong" )
			strong[0].string = headings[i]

	
	ps = soup.find_all( "p", {"class": "texts-go-in-here"} )
	
	for ind, p in enumerate( ps ) : 
		p.string = texts[ind]
			
			
	# creating a draft using current htmnl 
	create_draft( str(soup), email, 'Resume Rumble Evaluation' )



def injectData( leader, teamid, password, email ):
	html =""

	with open("idea.html", "r") as base_html:
		html = base_html.read()

	soup = Soup( html, features="html.parser" )

	# setting leader name
	div = soup.find_all("p", {"id": "leader_name"})
	div[0].string = "Dear " + leader + ","

	# setting team id
	details_div = soup.find(id="team_details")
	div2 = details_div.find_all( "p" )
	div2[0].string = "Team ID: " + teamid
	div2[2].string = "Password: " + password	
			
	# creating a draft using current htmnl 
	create_draft( str(soup), email, "[IMPORTANT] Hack Matrix 2.0 Team Leader Login Credentials | PCCOE's GeeksforGeeks Student Chapter | ARTIMAS 2024" )


# testing the module
if __name__ == "__main__":	
	# reading the CVS file
	# df = pd.read_csv("data.csv")
	
	# count = 0 
	# w= 0

	# for (idx, row) in df.iterrows():
		# l = []
		# texts = []
		
	# 	if( row["Email Address"] == "sarthak.kshirsagar22@pcooepune.org"):
	# 		if( str( row["Remark"] ) == "nan" ):
	# 			l.append( row["Email Address"])
	# 			l.append( row["Score"] )
	# 			l.append( int( row["Impact"] ) )
	# 			l.append( int( row["Brevity"] ) )
	# 			l.append( int( row["Style"] ) )
	# 			l.append( int( row["Sections"] ) )

	# 			texts.append( row["Impact Text"] )
	# 			texts.append( row["Brevity Text"] )
	# 			texts.append( row["Style Text"] )
	# 			texts.append( row["Sections Text"] )

	# 			count += 1		
	# 			create_html_content( *l, texts )
	# 		else:
	# 			print( row["Name"], "-> " , row["Remark"])
	# 			w+=1

	# print( count )
	# print( w )



	df = pd.read_csv("registrations.csv")
	for (idx, row) in df.iterrows():
		values = []
		values.append( row["Leader"] )
		values.append( row["Team Id"] )
		values.append( "HACKMATRIX")

		email = row["Email"]
		injectData( *values, email )