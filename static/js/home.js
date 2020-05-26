$('#cityform').on('submit',function(e){
	e.preventDefault();
	city=$('#cityselect').val()
	date=$('#citydate').val()
	date1=$('#citydate1').val()
	data={'city':city,'date':date,'date1':date1}
	$('.loader').show();
	$.ajax({
	 url:'/send',
	 type:'POST',
	 contentType: 'application/json',
	 data:JSON.stringify(data),
	 success:function(response){
	 $('#hidetable').hide();
	  var res=JSON.parse(response);
	  var table1=res['table1']
	  var table2=res['table2']
	   $('#cityname').html(table1['city'])
	  $('#cityregion').html(table1['region'])
	  $('#timezone').html(table1['timezone'])
		$('#longitude').html(table1['long'])
		$('#latitude').html(table1['lat'])


	  var tabledata=''
	  tabledata+='<table style="width:100%" class="table table-condensed">'
	   tabledata+='<tr><th>Date</th><th>Dawn</th><th>Sunrise</th><th>Noon</th><th>Sunset</th><th>Dusk</th></tr>'
           
	 
		for(var i=0;i<table2.length;i++){
			tabledata+='<tr><td>'+table2[i]['date']+'</td><td>'+table2[i]['dawn']+'<td>'+table2[i]['sunrise']+'</td><td>'+table2[i]['noon']+'</td><td>'+table2[i]['sunset']+'</td><td>'+table2[i]['dusk']+'</td></tr>'
		}
		tabledata+='</table>'

		$('#tablesss').html(tabledata)


	 }
});

});

