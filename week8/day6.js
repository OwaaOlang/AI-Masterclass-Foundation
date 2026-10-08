//Replicate Javascript array method
let fruits = ['mango', 'banana', 'apple']

// In JavaScript
fruits.push('grape');   // add to an end
console.log(fruits);

console.log(fruits.pop());  // removes first
console.log(fruits.length);  // 

console.log(fruits.shift());  // removes last
console.log(fruits);


//fetch data


const fetchData = async(url) => {
    try{
        const response = await fetch(url)

        if (!response.ok) {throw new Error (`HTTP error: ${response.status}`);
    }
    
    const data = await response.json()
    console.log(data)
    console.log('STATUS: OK')
    console.log('Origin IP:', data.origin)

} catch(err) {
    console.error("fetch Failed:", err.message);
  }
};

fetchData('https://httpbin.org/get');



//

obj = {"tool": "AI Summariser", "version": 1, "active": True}


const obj= {"tool": "AI Summariser", "version": 1, "active": True}

let js_string= JSON.stringify(obj);
console.log("Serialized:", js_string);

let parsed = JSON.parse(js_string);
console.log("total name:", parsed.tool);


//build a simple data fetcher

const fetchAndFormat = async(url) => {
    const response = await fetch(url)
    const data = await response.json()

    let formatted={
        "tool": "AI Summariser",
        status: "success",
        origin: data.origin,
        url: data.url

    };
    return JSON.stringify(formatted, null, 2);
};

fetch = ("https://httpbin.org/get")
   .then(response => response.json());
   .then(data => console.log(JSON.stringify(data, null, 2)));

//
function greetUser(name) {
    return `Welcome ${name}! Ready to build?`;
}
console.log(greetUser("Denis"));
console.log(greetUser("Owaa"));

//
const weeks = [
  { amount_spent: 8000,  texts_sent: 40, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 55, texts_replied: 3 },
  { amount_spent: 9000,  texts_sent: 38, texts_replied: 4 },
  { amount_spent: 11000, texts_sent: 42, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 35, texts_replied: 3 },
];

let totalSpent = 0;
let totalSent = 0;
let totalReplied = 0;

for (let week of weeks) {
    totalSpent += week.amount_spent;
    totalSent += week.texts_sent;
    totalReplied += week.texts_replied;
}
let replyRate = Math.round((totalReplied / totalSent) *100);

let verdict = "";
if (replyRate < 20) {
    verdict = "Cut your losses";
} else if (repyRate < 50) {
    verdict = "She might like you";
}else {
    verdict = "Keep going";
}

console.log(`Total spent: KES ${totalSpent}`);
console.log(`Texts sent: ${totalSent}`);
console.log(`Replies received: ${totalReplied}` )
console.log(`Reply rate: ${replyRate}%`);
console.log(`Verdict: ${verdict}`);
