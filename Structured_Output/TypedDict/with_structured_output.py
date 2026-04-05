from typing import TypedDict, Annotated ,Optional , Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()


class review(TypedDict):
    summary:str
    sentiment:str

#Annotated
class review(TypedDict):

    key_themes:Annotated[list[str],'Write down all the key themes discusses in the review in a list']
    summary:Annotated[str,'A brief summary of the review']
    sentiment:Annotated[Literal['pos','neg'],'Return sentiment of the review either negative,positive,neutral']
    pros:Annotated[Optional[list[str]],'Write down all the pros inside a list']
    cons:Annotated[Optional[list[str]],'Write down all the cons inside a list']
    name:Annotated[Optional[str],'write the name of the reviewe r ']
structured_model=model.with_structured_output(review)




result=structured_model.invoke('I recently started using the Samsung Galaxy S24 Ultra, and overall, it feels like a premium device built for performance. The Snapdragon 8 Gen 3 chipset delivers extremely smooth performance—whether I’m switching between apps, playing heavy games, or working on photo edits, everything runs effortlessly without lag.

Battery performance is another strong point. The 5000mAh battery comfortably gets me through an entire day, even with intensive usage. Plus, the fast charging support makes it easy to quickly top up when needed.

The S-Pen is a nice addition, especially for quick notes or occasional creative work, although I personally don’t use it all the time. The standout feature for me is definitely the camera system. The 200MP sensor captures highly detailed photos, and low-light shots come out surprisingly clear and vibrant. The zoom feature is impressive too—usable up to around 30x, but quality starts dropping if pushed further.

On the downside, the phone is quite large and slightly heavy, which makes handling it with one hand a bit inconvenient. Also, the One UI still includes several pre-installed apps that feel unnecessary, especially when similar Google apps are already available. Lastly, the pricing is on the higher side, which might not suit everyone.

Pros:
Extremely fast and powerful performance
High-quality 200MP camera with excellent zoom
Strong battery life with fast charging support
Unique S-Pen functionality

Review by Dilpreet Singh')
print(result)

print(result['summary'])
print(result['sentiment'])