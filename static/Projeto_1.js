function mes() {

	var p  = document.createElement('p');
	p.className = 'mes';
	p.appendChild(document.createTextNode('Janeiro'));
	document.getElementById('mes').appendChild(p);

}


function dias_semana() {

	var ul = document.createElement('ul');
	semana = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado']
	

	for(var j=0;j<7;j++){
		 var dia_semana = document.createElement('p');
		 dia_semana.className = "dia_semana";
		 dia_semana.appendChild(document.createTextNode(semana[j]));
		 document.getElementById('titulos_semana').appendChild(dia_semana);
		 ul.appendChild(dia_semana);

	}

	document.getElementById('titulos_semana').appendChild(ul);

}


function desenho() {

	var ul = document.createElement('ul');
	var counter_semana = 1;
	
	
	for(var i=0;i<30;i++){

		 var li = document.createElement('li');
		 li.className = 'dias'; 
		 li.appendChild(document.createTextNode(i+counter_semana));
		 var a = document.createElement('a');
		 a.appendChild(li);
		 a.setAttribute("href", "/" + "?Dia=" + (1 + i));
		 ul.appendChild(a);
		 li.setAttribute("id", "Dia" + (1 + i));
		 
		 counter_semana = 1;

	}

    document.getElementById('calendario').appendChild(ul);
    
}