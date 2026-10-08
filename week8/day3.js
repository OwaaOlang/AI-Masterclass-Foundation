

//API 
const fetchData = async(url)=> {
    const response = await fetch(url);
    if (!response.ok) throw new Error (`HTTP ${response.status}`);
    console.log(await response.json());
};

    //POST
    const postData = async(url, data)=> {
      const response = await fetch(url, {
        method: "POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    console.log(await response.json());
};




//python backend
app =  FASTAPI()

app.add_middleware(
    CORSmiddleware,
    allow_origin=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

checkins = []

class checkIn(BaseModel):
    name: str
    sleep: Float
    water: Int
    steps: Int


app.get("/api/checkins")
def get_checkins():
    return checkins 


app.post("/api/checkins")
def add_checkin(data: checkin):
entry = data.dict ()
entry["hit_goal"] = data.steps>=10000
checkins.append(entry)
return {"success" : true, "stored": entry}








