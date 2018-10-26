# Mājas darbs I

### Students: Karina Pilusonoka, kp14012

## Setup
* Run `python parser.py`
* from mongo repl run `db.loadServerScripts()`
  
## Available functions for reports
* `report_TasterExpirience` - will prepare report about tasters expirience (demonstration of `mapReduce` )
* `q_getMostExpiriencedTasters` - will show most expirienced of them (demonstration of understanding `sort`, `limit`)
* `q_relationBetweenQualityAndPrice` - will answer to the question **"Does it really exists correlation between wine quality and its price?"** (short answer: Yes) (demonstration of `$aggregate`, `$match`, `$project`, `$group`, `$concat`, `$cond`, `$avg`, `$sum`, etc..)
* `q_bestWinePerRange` - will return 5 best wines per price range (demonstration of usage aggregated values as properties for next grouping)

* `q_bestWineRate` - will show which country have best wine quality + average price (personal interest)

## Hints
* For readable queries check `wines.system.orig.json`