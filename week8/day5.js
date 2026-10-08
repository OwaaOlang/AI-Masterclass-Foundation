
//predict with confidence score and coaching message
// steps, sleep and water

const predictgoal = (sleep, water, steps)=> {
    const sleepscore = Math.min(sleep/ 8.0, 1) *35
    const waterscore = Math.min(water/10.0, 1) * 25
    const stepsscore = Math,min(steps/12000, 1)* 40

    const score = sleepscore + waterscore + stepsscore;

    return{
        hitGoal = score>= 60,
        confidence: score/100,
        score: Math.round(score)
    }
}