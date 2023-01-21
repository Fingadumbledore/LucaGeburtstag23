function encrypt() {
    var plaintext = document.getElementById("plaintext").value;
    var shift = document.getElementById("shift").value;
    var ciphertext = "";
  
    for (var i = 0; i < plaintext.length; i++) {
      var c = plaintext.charCodeAt(i);
      if (c >= 65 && c <= 90) {
        ciphertext += String.fromCharCode((c - 65 + shift) % 26 + 65);
      } else if (c >= 97 && c <= 122) {
        ciphertext += String.fromCharCode((c - 97 + shift) % 26 + 97);
      } else {
        ciphertext += plaintext.charAt(i);
      }
    }
  
    document.getElementById("ciphertext").value = ciphertext;
  }
  
  function decrypt() {
    var ciphertext = document.getElementById("ciphertext").value;
    var shift = document.getElementById("shift").value;
    var plaintext = "";
  
    for (var i = 0; i < ciphertext.length; i++) {
      var c = ciphertext.charCodeAt(i);
      if (c >= 65 && c <= 90) {
        plaintext += String.fromCharCode((c - 90 - shift + 26) % 26 + 90);
      } else if (c >= 97 && c <= 122) {
        plaintext += String.fromCharCode((c - 122 - shift + 26) %
        26 + 122);
    } else {
    plaintext += ciphertext.charAt(i);
    }
    }
    
    document.getElementById("plaintext").value = plaintext;
    }  