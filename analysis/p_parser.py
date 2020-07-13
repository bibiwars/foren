########################### import p_parser
import json
def json_parse_html(plugin, path):
	#print "++++parsing json to html"
	html = '<html>'
	html += '<head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"></head>'
	html += '<body><table id="myTable" class="table table-striped table-sm">'

	#json to html
	with open(path + plugin + '.json') as f:
		data = json.load(f)
		
		html += '<thead class="thead-dark"><tr>'
		col_id = 0
		for col in data['columns']:
			html += '<th onclick="sortTable('+ str(col_id) +')">' + str(col) + '</th>'
			col_id+=1
		html += '</tr></thead>'

		for row in data['rows']:
			html += '<tbody><tr>'
			for i in row:
				if isinstance(i, (int, long)):
					i = str(i)
				html += '<td>' + i.encode('ascii','replace') + '</td>'
			html += '</tr>'
			
	html += '''</tbody></table>
	<script>
	function sortTable(n) {
	  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
	  table = document.getElementById("myTable");
	  switching = true;
	  //Set the sorting direction to ascending:
	  dir = "asc";
	  /*Make a loop that will continue until
	  no switching has been done:*/
	  while (switching) {
		//start by saying: no switching is done:
		switching = false;
		rows = table.rows;
		/*Loop through all table rows (except the
		first, which contains table headers):*/
		for (i = 1; i < (rows.length - 1); i++) {
		  //start by saying there should be no switching:
		  shouldSwitch = false;
		  /*Get the two elements you want to compare,
		  one from current row and one from the next:*/
		  x = rows[i].getElementsByTagName("TD")[n];
		  y = rows[i + 1].getElementsByTagName("TD")[n];
		  /*check if the two rows should switch place,
		  based on the direction, asc or desc:*/
		  if (!isNaN(x.innerHTML)){
		  	  if (dir == "asc") {
				if (Number(x.innerHTML) > Number(y.innerHTML)) {
				  //if so, mark as a switch and break the loop:
				  shouldSwitch= true;
				  break;
				}
			  } else if (dir == "desc") {
				if (Number(x.innerHTML) < Number(y.innerHTML)) {
				  //if so, mark as a switch and break the loop:
				  shouldSwitch = true;
				  break;
				}
			  }
		  }else{
			  if (dir == "asc") {
				if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
				  //if so, mark as a switch and break the loop:
				  shouldSwitch= true;
				  break;
				}
			  } else if (dir == "desc") {
				if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
				  //if so, mark as a switch and break the loop:
				  shouldSwitch = true;
				  break;
				}
			  }
		  }
		}
		if (shouldSwitch) {
		  /*If a switch has been marked, make the switch
		  and mark that a switch has been done:*/
		  rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
		  switching = true;
		  //Each time a switch is done, increase this count by 1:
		  switchcount ++;      
		} else {
		  /*If no switching has been done AND the direction is "asc",
		  set the direction to "desc" and run the while loop again.*/
		  if (switchcount == 0 && dir == "asc") {
		    dir = "desc";
		    switching = true;
		  }
		}
	  }
	}
	</script>
		</body></html>'''
	
	out = open(path + plugin + '.html','w+')
	out.write(html)
	out.close()
#########################################
