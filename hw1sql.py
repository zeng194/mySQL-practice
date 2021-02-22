import sys

# Use this file to write your queries. Submit this file in Brightspace after finishing your homework.

#TODO: Write your username and answer to each query as a string in the return statements in the functions below. 
# Do not change the function names. 

#Your resulting tables should have the attributes in the same order as appeared in the sample answers. 

#Make sure to test that python prints out the strings (your username and SQL queries) correctly.

#usage: python hw1.py

def username():
	return "zeng194"

def query1():
	return "SELECT COUNT(sc_level) as sc_count FROM securityclearance"

def query2():
	return "SELECT city ,count(city) as agent_count, AVG(salary) as average_salary FROM agent WHERE city LIKE 'A%' GROUP BY city"

def query3():
	return "SELECT city ,count(city) as agent_count, AVG(salary) as average_salary FROM agent WHERE city LIKE 'A%' GROUP BY city HAVING count(city) >= 5"
	
def query4():
	return "SELECT DISTINCT a.first, a.last, a.salary, count(s.agent_id) as skill_count, a.salary/count(s.agent_id) as ratio FROM skillrel s JOIN agent a on s.agent_id = a.agent_id GROUP BY s.agent_id HAVING a.salary/count(s.agent_id) < 10100"

def query5():
	return "SELECT a.first, a.last, a.city, a.salary, b.first, b.last, b.salary, b.city FROM agent a JOIN agent b on a.city = b.city AND a.salary = b.salary AND a.agent_id != b.agent_id"

def query6():
	return "SELECT DISTINCT t.name, ss.skill FROM skill ss, team t, skillrel s, teamrel tr WHERE t.name like 'BLACKOUT' AND tr.team_id = 10 AND s.agent_id = tr.agent_id AND ss.skill_id = s.skill_id "

def query7():
	return "(SELECT DISTINCT l.language FROM agent a JOIN mission m on m.access_id = a.clearance_id JOIN languagerel lr on lr.agent_id = a.agent_id JOIN skillrel sr on a.agent_id = sr.agent_id JOIN language l on l.lang_id = lr.lang_id JOIN skill s on s.skill_id = sr.skill_id WHERE m.name LIKE 'Media Blanket') UNION (SELECT DISTINCT s.skill FROM agent a JOIN mission m on m.access_id = a.clearance_id JOIN languagerel lr on lr.agent_id = a.agent_id JOIN skillrel sr on a.agent_id = sr.agent_id JOIN language l on l.lang_id = lr.lang_id JOIN skill s on s.skill_id = sr.skill_id WHERE m.name LIKE 'Media Blanket')"
def query8():
	return "SELECT a.first, a.last, f.title FROM agent a LEFT OUTER JOIN affiliationrel ar on a.agent_id = ar.agent_id LEFT OUTER JOIN affiliation f on f.aff_id = ar.aff_id WHERE EXISTS(SELECT * FROM agent a, affiliationrel ar WHERE a.agent_id = ar.agent_id) AND a.city LIKE 'Sao Paolo'"
	
def query9():
	return "SELECT COUNT(DISTINCT lr.lang_id) as languages FROM agent a JOIN languagerel lr on a.agent_id = lr.agent_id JOIN affiliationrel ar on a.agent_id = ar.agent_id WHERE ar.aff_id = 8 AND (ar.affiliation_strength LIKE 'Medium' OR ar.affiliation_strength LIKE 'Strong')"

def query10():
	return "SELECT a.agent_id, a.first, a.last, MAX(salary) FROM agent a JOIN affiliationrel ar on a.agent_id = ar.agent_id WHERE a.salary = (SELECT MAX(b.salary) FROM agent b JOIN affiliationrel br on b.agent_id = br.agent_id WHERE br.aff_id = 9)"

def query11():
	return "SELECT avg(ratio) as average_ratio FROM (SELECT DISTINCT a.salary/count(s.agent_id) as 'ratio' FROM skillrel s JOIN agent a on s.agent_id = a.agent_id GROUP BY s.agent_id) as temp"

def query12():
	return "SELECT l.language, COUNT(l.language) as count_of_agents FROM agent a JOIN languagerel lr on a.agent_id = lr.agent_id JOIN language l on lr.lang_id = l.lang_id GROUP BY (l.language) HAVING COUNT(l.language) <= 0.15 * (SELECT COUNT(b.agent_id) FROM agent b)"

#Do not edit below

def main():
	query_options = {1: query1(), 2: query2(), 3: query3(), 4: query4(), 5: query5(), 6: query6(), 7: query7(), 8: query8(), 
		9: query9(), 10: query10(), 11: query11(), 12: query12()}
	
	if len(sys.argv) == 1:
		if username() == "username":
			print("Make sure to change the username function to return your username.")
			return
		else:
			print(username())
		for query in query_options.values():
			print(query)
	elif len(sys.argv) == 2:
		if sys.argv[1] == "username":
			print(username())
		else:
			print(query_options[int(sys.argv[1])])

	
if __name__ == "__main__":
   main()
