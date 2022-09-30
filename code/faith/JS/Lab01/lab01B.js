let enter = document.getElementById('enter');





enter.addEventListener('click', function(){
    let codeword = document.querySelector('#codeword');
    let word = document.querySelector('#word').value;
    console.log('hello')
    let rot13 = {
        a:'n',
        b:'o',
        c:'p',
        d:'q',
        e:'r',
        f:'s',
        g:'t',
        h:'u',
        i:'v',
        j:'w',
        k:'x',
        l:'y',
        m:'z',
        n:'a',
        o:'b',
        p:'c',
        q:'d',
        r:'e',
        s:'f',
        t:'g',
        u:'h',
        v:'i',
        w:'j',
        x:'k',
        y:'l',
        z:'m',
        ' ':' ',
        A:'N',
        B:'O',
        C:'P',
        D:'Q',
        E:'R',
        F:'S',
        G:'T',
        H:'U',
        I:'V',
        J:'W',
        K:'X',
        L:'Y',
        M:'Z',
        N:'A',
        O:'B',
        P:'C',
        Q:'D',
        R:'E',
        S:'F',
        T:'G',
        U:'H',
        V:'I',
        W:'J',
        X:'K',
        Y:'L',
        Z:'M',
    }   
    codewordList =[]
    
    for (let letter in word) {
        let test = word[letter]
        codewordList.push(rot13[test])
        console.log(test)
    }
    
    codeword.innerHTML = codewordList.join('')
})
// enter.onclick = function() {
//     let newword = word.value;
