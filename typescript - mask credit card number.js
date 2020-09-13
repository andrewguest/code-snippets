/*
This will take an input (a credit card number) and, if it's over 4 digits long, replace all but the LAST four digits with '#'.

So, 1234567890123456 becomes ############3456
*/

function maskCreditCardNumber(cc: string): string {
  let masked_cc = cc.replace(/\d(?=\d{4})/g, "#");
  console.log(masked_cc);
  return masked_cc
}


// cc: string  means that the 'cc' input must be a string type.
// : string {   means that the function will return something that is a 'string'.
