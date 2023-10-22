'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}


/*
 * Complete the 'getTotalGoals' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING team
 *  2. INTEGER year
 */

const axios = require('axios');
async function getTotalGoals(team, year) {
    try{
        var ans=0,totalPage=1,t=1;
        while (t<=totalPage){
            const res1 = await axios.get('https://jsonmock.hackerrank.com/api/football_matches/',{
                params:{
                    year:year,
                    team1:team,
                    page:t
                }
            });
            totalPage=res1.data.total_pages;
            for (var item of res1.data.data){
                ans=ans+parseInt(item.team1goals);
            };
            t+=1;
        }
        var totalPage=1,t=1;
        while (t<=totalPage){
            const res2 = await axios.get('https://jsonmock.hackerrank.com/api/football_matches/',{
                params:{
                    year:year,
                    team2:team,
                    page:t
                }
            });
            totalPage=res2.data.total_pages;
            for (var item of res2.data.data){
                ans=ans+parseInt(item.team2goals);
            };
            t+=1;
        }
        return ans;
    }catch(error){
        console.error(error)
    }
}
async function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const team = readLine();

    const year = parseInt(readLine().trim(), 10);

    const result = await getTotalGoals(team, year);

    ws.write(result + '\n');

    ws.end();
}
