$('#cityform').on('submit',function(e){
	e.preventDefault();
	city=$('#cityselect').val()
	date=$('#citydate').val()
	data={'city':city,'date':date}

	$.ajax({
	 url:'/send',
	 type:'POST',
	 contentType: 'application/json',
	 data:JSON.stringify(data),
	 success:function(response){
	  var res=JSON.parse(response);
	  var table1=res['table1']
	  var table2=res['table2']
	  console.log(table2)
	  $('#cityname').html(table1['city'])
	  $('#cityregion').html(table1['region'])
	  $('#timezone').html(table1['timezone'])
		$('#longitude').html(table1['long'])
		$('#latitude').html(table1['lat'])
		$('#tablesss').html('<td>'+table2['date']+'</td><td>'+table2['dawn']+'<td>'+table2['sunrise']+'</td><td>'+table2['noon']+'</td><td>'+table2['sunset']+'</td><td>'+table2['dusk']+'</td>')


	 }
});

});

