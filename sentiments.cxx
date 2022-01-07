#encoding "utf-8"

Persons -> AnyWord<kwtype="люди">;  
Sights -> AnyWord<kwtype="объекты">;  

Data -> Persons interp (Data.Person_output) (Word<gram="дат">);
		
Data ->	Sights interp (Data.Object_output) (Word<gram="дат">);