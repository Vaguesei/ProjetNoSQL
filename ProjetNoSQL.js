db.market.aggregate([ {$group : { _id : "$quarter", total :{$sum:1} }}])

db.store.aggregate([ {$group : { _id : "$quarter", total :{$sum:1} } }, {$sort : {total : -1}}])