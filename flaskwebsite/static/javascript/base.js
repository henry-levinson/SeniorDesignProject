// base.js
// Add your custom JavaScript code here
document.addEventListener('DOMContentLoaded', function() {
    // Add click event listener to gene name links
    var geneNameLinks = document.getElementsByClassName('gene-name');
    for (var i = 0; i < geneNameLinks.length; i++) {
      geneNameLinks[i].addEventListener('click', function(event) {
        event.preventDefault();
        var geneName = this.innerHTML;
        var geneValues = this.parentNode.parentNode.cells; // Get values from the same row as gene name
  
        // Open a new window with gene information
        var popup = window.open('', 'Gene Information', 'width=500,height=400');
        popup.document.body.innerHTML = '<h1>Gene Name: ' + geneName + '</h1>';
        popup.document.body.innerHTML += '<p>Score: ' + geneValues[1].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>Principal Findings: ' + geneValues[2].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>Methodology: ' + geneValues[3].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>UNIPROTKB_AC: ' + geneValues[4].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>UNIPROTKB_ID: ' + geneValues[5].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>Description: ' + geneValues[6].innerHTML + '</p>'; // Updated line
        popup.document.body.innerHTML += '<p>Ensembl: ' + geneValues[7].innerHTML + '</p>'; // Updated line
        popup.document.body.innerHTML += '<p>HGNC: ' + geneValues[8].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>PDB: ' + geneValues[9].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>PDB ID: ' + geneValues[10].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>GTEx: ' + geneValues[11].innerHTML + '</p>';
        popup.document.body.innerHTML += '<p>ExpresionAltas: ' + geneValues[12].innerHTML + '</p>';
      });
    }
  });
  