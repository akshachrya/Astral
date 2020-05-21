var a=$('#cityform')


a.on('submit',function(e){
	e.preventDefault();
	city=$('#cityselect').val()
	date=$('#citydate').val()
	data={'city':city,'date':date}

	$.ajax({
	 url:'/send',
	 type:'POST',
	 contentType: 'application/json',
	 data:data,
	 success:function(response){
	  // var res=JSON.parse(response);

	 }
});

});

