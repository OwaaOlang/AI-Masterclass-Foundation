
// predict with confidence score and coaching message
// steps, sleep and water

const predictGoal = (sleep, water, steps) => {
  const sleepScore = Math.min(sleep / 8.0, 1) * 35
  const waterScore = Math.min(water / 10.0, 1) * 25
  const stepsScore = Math.min(steps / 12000, 1) * 40

  const score = sleepScore + waterScore + stepsScore;

  return {
    hitGoal: score >= 60,
    confidence: score / 100,
    score: Math.round(score)
  };
};

const COACHING = {
  "111": ["strong input, strong output. strong baseline"],
  "110": ["hit goal despite low water. close hydration gap tomorrow"],
  "101": ["water carried today despite low sleep. shore up sleep"],
  "100": ["Goal hit on willpower. Build foundation of sleep and water intake"],
  "011": ["solid inputs. But goal missed, audit scheduled"],
  "010": ["sleep solid. water low, goal missed, add 2 glasses of water"],
  "001": ["Low sleep is the primary issue. get to bed earlier"],
  "000": ["Both inputs low and goal missed"]
};

const getCoaching = (sleep, water, hitGoal) => {
  const key = `${hitGoal? 1 : 0}${sleep >= 7? 1 : 0}${water >= 8? 1 : 0}`;
  return COACHING[key].join("");
}

// --- MAKE IT RUN ---
const test = predictGoal(6, 6, 8000);
const message = getCoaching(6, 6, test.hitGoal);

console.log(test);
console.log("Coaching:", message);
