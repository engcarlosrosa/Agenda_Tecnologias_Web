


function desenho() {

	var ul = document.createElement('ul');
	var p  = document.createElement('p'); 
	dias_semana = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado']
	meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
	var counter_semana = 0;
	var counter_mes = 30;



	for(var i=0;i<30;i++){
		 var li = document.createElement('li');
		 li.className = 'semana'; 
		 li.appendChild(document.createTextNode(dias_semana[i - counter_semana]));
		 var a = document.createElement('a');
		 a.appendChild(li);
		 a.setAttribute("href", "/" + "?Dia=" + (1 + i))
		 ul.appendChild(a);
		 li.setAttribute("id", "Dia" + (1 + i));
		 
		 
		 
		 if(dias_semana[i - counter_semana] == 'Sábado'){
		  counter_semana+=7;


		 }

	}

	p.className = 'mes';
	p.appendChild(document.createTextNode('Janeiro'));
	document.getElementById('calendario').appendChild(p);
	document.getElementById('calendario').appendChild(ul);

}
  

