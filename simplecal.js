function calculator( a , b , operator) {
    switch(operator){
        case "+":
            return a+b;
        case "-":
            return a-b;
        case "*":
            return a*b;
        default :
        return "invalid our data";
         
    }


}

console.log(calculator( 1 , 8 , "+"))

