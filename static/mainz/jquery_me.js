// JavaScript Document


	function checkIfIsEmail(){
		var email = $("#email").val();
		
		if(email == ""){
			$("#email_error").hide()
		}
		
		if(email != ""){
			
			isEmail = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/.test(email);
			if(!isEmail){
				$("#email_error").show(500)
				$("#email_error").text("Please Enter a valid email Address")
			}else{
				$("#email_error").text("")
				$("#email_error").attr("hidden", "hidden")
			}
			
		}
		
		
	}


	


	function passwordStrength(password)
	{
		var desc = new Array();
		desc[0] = "Very Weak";
		desc[1] = "Weak";
		desc[2] = "Better";
		desc[3] = "Medium";
		desc[4] = "Strong";
		desc[5] = "Strongest";

		var score   = 0;

		//if password bigger than 6 give 1 point
		if (password.length > 6) score++;

		//if password has both lower and uppercase characters give 1 point	
		if ( ( password.match(/[a-z]/) ) && ( password.match(/[A-Z]/) ) ) score++;

		//if password has at least one number give 1 point
		if (password.match(/\d+/)) score++;

		//if password has at least one special caracther give 1 point
		if ( password.match(/.[!,@,#,$,%,^,&,*,?,_,~,-,(,)]/) )	score++;

		//if password bigger than 12 give another 1 point
		if (password.length > 12) score++;

		 document.getElementById("passwordDescription").innerHTML = desc[score];
		 document.getElementById("passwordStrength").className = "strength" + score;
	}
	

	function checkIfIsPhone(){
		var phone = $("#phone").val();
		
		if(phone == ""){
			$("#phone_error").hide()
		}
		
		if(phone != ""){
			
			var intRegex = /^\d+$/;
			if(!intRegex.test(phone)){
				$("#phone_error").show(500)
				$("#phone_error").text("Please Enter Numbers Only")
			}else{
				$("#phone_error").text("")
				//$("#phone_error").hide()
				$("#phone_error").attr("hidden", "hidden")
			}
			
		}
		
		
	}

	function checkAlphaNumeric(a){
		var alphaNum = /^[a-z0-9]+$/i;
		var testThis = $(a).val();
		var report = $(a).prev().val();
		if(!alphaNum.test(testThis)){
			$(a).closest("div").next("div").find("div").show(500)
			$(a).closest("div").next("div").find("div").text(report + "must be alpha-numeric");
		}else if(testThis != ""){
			$(a).closest("div").next("div").find("div").hide()
		}
	}
	
	function checkUsername(){//checks if phone no exist on blur
		
		var phone_send = $('#username').val();
	
		
				if(phone_send !== ""){
						
							$.post("jquery_check.php",$("#username").serialize(),function(data, status){
										if(status == "success"){
											 if (data == "1"){
												$("#user_error").show(500);
												$("#user_error").text("Username already exists");
												
											 }else{
												 
												$("#user_error").attr("hidden", "hidden")
												$("#user_error").text("");
												 
											 }
										}
								
							});
									
								
							
						
				}else{
					$("#user_error").show(500);
					$("#user_error").text("Please fill in the fields");
				}
	}
			
			
	function checkPhoneNo(){//checks if phone no exist on blur
		
		var phone_send = $('#phone').val();
	
		
				if(phone_send !== ""){
						
							$.post("jquery_check.php",$("#phone").serialize(),function(data, status){
										if(status == "success"){
											 if (data == "1"){
												$("#phone_error").show(500);
												$("#phone_error").text("Phone Number Exists");
												
											 }else{
												 
												$("#phone_error").attr("hidden", "hidden")
												$("#phone_error").text("");
												
											 }
										}
								
							});
									
								
							
						
				}else{
					$("#phone_error").show(500);
					$("#phone_error").text("Please fill in the fields");
				}
	}
			
			
	function checkEmail(){//checks if phone no exist on blur
		
		var email = $('#email').val();
		
				if(email !== ""){
						
							$.post("jquery_check.php",$("#email").serialize(),function(data, status){
										if(status == "success"){
											 if (data == "1"){
												$("#email_error").show(500);
												$("#email_error").text("Email Exists");
												 
											 }else{
												 
												$("#email_error").attr("hidden", "hidden")
												$("#email_error").text("");
												 
											 }
										}
								
							});
									
								
							
						
				}else{
					$("#email_error").show(500);
					$("#email_error").text("Please fill in the fields");
				}
	}
			
	function checkPassword(){
		var password = $("#password").val()
		var con_password = $("#password2").val()
		
		if((password != "") || (con_password != "")){
			
			if(password != con_password){
				$("#pass_error").show()
				$("#con_pass_error").show()
				$("#pass_error").text("Passwords does not match").css({"color": "red"});
				$("#con_pass_error").text("Passwords does not match").css({"color": "red"});
				$("#password").css({"background-color":"white", "border-color": "red", "border-width":"1px", "border-style":"solid"});
				$("#password2").css({"background-color":"white", "border-color": "red", "border-width":"1px", "border-style":"solid"});
				
			}else{
				
				$("#pass_error").hide()
				$("#con_pass_error").show()
				$("#con_pass_error").text("Passwords match")
				$("#con_pass_error").css({"color": "#00CC66"});
				$("#password").css({"background-color":"#00CC66", "border-color": "#CCCCCC", "border-width":"1px", "border-style":"solid"});
				$("#password2").css({"background-color":"#00CC66", "border-color": "#CCCCCC", "border-width":"1px", "border-style":"solid"});
				
				setTimeout(function(){
					$("#pass_error").hide()
					$("#con_pass_error").hide()
					$("#password").css({"background-color":"white"});
					$("#password2").css({"background-color":"white"});
				},5000);
			}
			
		}
	}
	
			
	function checkPLenght(){
		var password = $("#password").val()
		
		
			if(password.length < "8"){
				$("#pass_error").show()
				$("#pass_error").text("password must be equal to or more than 8 characters and alpha numeric")
			}else{
				$("#pass_error").hide()
			}
		
			var alphaNum = /^[a-z0-9]+$/i;
			var testThis = $(a).val();
			var report = $(a).prev().val();
			if(!alphaNum.test(testThis)){
				$(a).closest("div").next("div").find("div").show(500)
				$(a).closest("div").next("div").find("div").text(report + "must be alpha-numeric");
			}else if(testThis != ""){
				$(a).closest("div").next("div").find("div").hide()
			}
	}
			
	function checkIfIsNo(){
		var acct_no = $("#acct_no").val();
		
		if(acct_no == ""){
			$("#account_error").hide()
		}
		
		if(acct_no != ""){
			
			var intRegex = /^\d+$/;
			if(!intRegex.test(acct_no)){
				$("#account_error").show(500)
				$("#account_error").text("Please Enter Numbers Only")
			}else if(acct_no.length < "10"){
				$("#account_error").show(500)
				$("#account_error").text("Account Number must be equal 10")
			}else if(acct_no.length > "10"){
				$("#account_error").show(500)
				$("#account_error").text("Account Number must be equal 10")
			}else{
				$("#account_error").text("")
				//$("#phone_error").hide()
				$("#account_error").attr("hidden", "hidden")
			}
			
		}
		
		
	}
			
	function checkname(){
		if($("#fullname").val() == ""){
			
			$("#name_error").show()
			$("#name_error").text("please enter your fullname").focus()
			
		}else{
			$("#name_error").hide()
		}
	}
			
	function checkAcctName(){
		if($("#account_name").val() == ""){
			
			$("#acct_name_error").show()
			$("#acct_name_error").text("please enter Your account name").focus()
			
		}else{
			$("#acct_name_error").hide()
		}
	}
			
	function checkAcctNo(){
		if($("#acct_no").val() == ""){
			
			$("#account_error").show()
			$("#account_error").text("please enter your account number").focus()
			
		}else{
			$("#account_error").hide()
		}
	}
			
	function checkBank(){
		if($("#bank").val() == "Select Bank"){
			
			$("#bank_error").show()
			$("#bank_error").text("please select a bank").focus()
			
		}else{
			$("#bank_error").hide()
		}
	}
			
	function checkCaptcha(){
		if($("#vercode2").val() == ""){
			
			$("#captcha_error").show()
			$("#captcha_error").text("please select captcha code").focus()
			
		}else{
			$("#captcha_error").hide()
		}
	}
			
	
			
	function submitSignUp(){
		
		if($("#email").val() == ""){
			
			$("#email_error").show()
			$("#email_error").text("please enter email address").focus()
			
		}else if($("#phone").val() == ""){
			
			$("#phone_error").show()
			$("#phone_error").text("please enter phone Number").focus()
			
		}else if($("#fullname").val() == ""){
			
			$("#name_error").show()
			$("#name_error").text("please enter your fullname").focus()
			
		}else if($("#username").val() == ""){
			
			$("#user_error").show()
			$("#user_error").text("please enter email address").focus()
			
		}else if($("#password").val() == ""){
			
			$("#pass_error").show()
			$("#pass_error").text("please enter Password").focus()
			
		}else if($("#password2").val() == ""){
			
			$("#con_pass_error").show()
			$("#con_pass_error").text("please confirm password").focus()
			
		}else if($("#account_name").val() == ""){
			
			$("#acct_name_error").show()
			$("#acct_name_error").text("please enter Your account name").focus()
			
		}else if($("#acct_no").val() == ""){
			
			$("#account_error").show()
			$("#account_error").text("please enter your account number").focus()
			
		}else if($("#bank").val() == "Select Bank"){
			
			$("#bank_error").show()
			$("#bank_error").text("please select a bank").focus()
			
		}else if($("#vercode2").val() == ""){
			
			$("#captcha_error").show()
			$("#captcha_error").text("please select captcha code").focus()
			
		}else{
			checkEmail()
			checkIfIsEmail()
			checkIfIsPhone()
			checkUsername()
			checkPhoneNo()
			checkPLenght()
			checkPassword()
			checkIfIsNo()
		}
		
	}
	
	//var a = document.getElementById("balance").value;
	
	
	
	
		
	
	function transferAmount(){	
		var main_amount = $("#reso").text();
		$("#display_reso").text(main_amount);
	}

	/*var a = document.getElementById("balance").value; 
	var main_amount = getThis(a); 
	document.getElementById("reso").innerHTML = main_amount;*/
	
	function callAmounter(){
		
		var main_amount = getThis(a);
		document.getElementById("reso").innerHTML = main_amount;
		
	}



	

	function getThis(c){
		
			var amount = c;
			
			var delimiter = ","; // replace comma if desired
			var a = amount.split('.',2)
			
			var d = a[1];
			var i = parseInt(a[0]);
			if(isNaN(i)) { return ''; }
			var minus = '';
			if(i < 0) { minus = '-'; }
			i = Math.abs(i);
			var n = new String(i);
			var a = [];
			while(n.length > 3) {
				var nn = n.substr(n.length-3);
				a.unshift(nn);
				n = n.substr(0,n.length-3);
			}
			if(n.length > 0) { a.unshift(n); }
			n = a.join(delimiter);
			
			
			if (typeof d == 'undefined'){
				amount = n;
			}else if(d.length < 1) { 
				amount = n; 
				
			}else { 
				amount = n + '.' + d;
			}
			amount = minus + amount;
			
			return amount;
			
		//}  
		//var ans = CommaFormatted(amount);
	}

//gets value from a div


function xmlHttpRequest(){
	
	var txt = "", txt1 = "";
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange=function() {
	  if (xmlhttp.readyState==4 && xmlhttp.status==200) {
		var response = JSON.parse(this.responseText); //if you need to do something with the returned v
		 //alert(response)
		 txt1 += "<marquee>";
		for (x in response) {
			
			for (j in response.quotes) {
				var r =j; 
				s = r.substr(0,3);
				k = r.substr(3,3);
				f = s + "/" + k;
				txt1 += f + ": " + response.quotes[j] + ". ";
			}
		}
		 txt1 += "</marquee>";
		
		document.getElementById("demo2").innerHTML = txt1;
	  }
	}
	
	xmlhttp.open("GET","http://apilayer.net/api/live?access_key=85e96ebb4e2fd17b9693a6221842fb3a",true);
	xmlhttp.send();
	
}
	
