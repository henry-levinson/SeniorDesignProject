document.addEventListener('DOMContentLoaded', function() {
  // Add click event listener to UNIPROTKB_AC links
  var uniprotkb_acLinks = document.getElementsByClassName('uniprotkb_ac');
  for (var i = 0; i < uniprotkb_acLinks.length; i++) {
    uniprotkb_acLinks[i].addEventListener('click', function(event) {
      event.preventDefault();
      var uniprotkb_ac = this.innerHTML;
      var uniprotkb_acValues = this.parentNode.parentNode.cells; // Get values from the same row as UNIPROTKB_AC

      // Open a new window with gene information
      var popup = window.open('', 'Gene Information', 'width=500,height=400');
      var popupContent = 
        '<h1>UNIPROTKB_AC: ' + uniprotkb_ac + '</h1>' +
        '<p>Score: ' + uniprotkb_acValues[0].innerHTML + '</p>' +
        '<p>Principal Findings: ' + uniprotkb_acValues[1].innerHTML + '</p>' +
        '<p>Methodology: ' + uniprotkb_acValues[2].innerHTML + '</p>' +
        '<p>UniProtKB_AC: ' + uniprotkb_acValues[3].innerHTML + '</p>' +
        '<p>UniProtKB_ID: ' + uniprotkb_acValues[4].innerHTML + '</p>' +
        '<p>Gene Name: ' + uniprotkb_acValues[5].innerHTML + '</p>' +
        '<p>Description: ' + uniprotkb_acValues[6].innerHTML + '</p>' +
        '<p>Ensembl: ' + uniprotkb_acValues[7].innerHTML + '</p>' +
        '<p>HGNC: ' + uniprotkb_acValues[8].innerHTML + '</p>' +
        '<p>PDB: ' + uniprotkb_acValues[9].innerHTML + '</p>' +
        '<p>PDB ID: ' + uniprotkb_acValues[10].innerHTML + '</p>' +
        '<p>GTEx: ' + uniprotkb_acValues[11].innerHTML + '</p>' +
        '<p>ExpresionAltas: ' + uniprotkb_acValues[12].innerHTML + '</p>';

      popup.document.body.innerHTML = popupContent;
    });
  }
});
