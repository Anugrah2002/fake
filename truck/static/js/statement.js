window.addEventListener("load", function() {
    statementDates = document.getElementsByClassName('statement-dates');

    for (let i=0;i<statementDates.length;i++){
        pays = document.getElementsByClassName('pay-amount-'+(i+1));
        n = pays.length;
        var totalPay =0
        for (let j=0;j<n;j++)
        {
        totalPay = totalPay+parseFloat(pays[j].innerText);
        }
        opening = (document.getElementById('pay-opening-'+(i+1)).innerText).split(" ")[0];
        totalPay = totalPay+converter(opening);
        document.getElementById('pay-total-'+(i+1)).innerHTML = totalPay.toFixed(2);

        try{
                recs = document.getElementsByClassName('rec-amount-'+(i+1));
                m = recs.length;
            var totalRec =0
                for (let k=0;k<m;k++)
                {
                totalRec = totalRec+parseFloat(recs[k].innerText);
                }
            }
        catch(err){
            totalRec = 0
        }
            document.getElementById('rev-total-'+(i+1)).innerHTML = totalRec.toFixed(2);
        // balance printing
        if (totalPay > totalRec){
             document.getElementById('rec-side-'+(i+1)).innerHTML = (totalPay-totalRec).toFixed(2)+"  available balance";
            document.getElementById("pay-opening-"+(i+2)).innerHTML =(totalPay-totalRec).toFixed(2)+"  opening balance";
            }
        else{
            document.getElementById('pay-side-'+(i+1)).innerHTML = (totalRec-totalPay).toFixed(2)+"  available balance";
            document.getElementById("rec-opening-"+(i+2)).innerHTML =(totalRec-totalPay).toFixed(2)+"  opening balance";
        }
    }
})

function converter(text){
    if (text == "")
        return parseFloat(0)
    else
        return parseFloat(text)
}