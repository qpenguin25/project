
conn = new Mongo();
db = conn.getDB("project");

var collections = db.getCollectionNames();
print('Collections inside the db:');
for(var i = 0; i < collections.length; i++){
  var name = collections[i];
  print(name)
  db.getCollection(name).find().forEach(function(x){
	                                    db.All_Comment.insert(x)
										})
}

conn = new Mongo();
db = conn.getDB("project");

var collections = db.getCollectionNames();
for(var i = 0; i < collections.length; i++){
	
	var name = collections[i];
	print (name)
	db.getCollection(name).mapReduce(function(){emit("",this.comment_collection.length)},
						 function(key,values){return Array.sum(values)},
						{
							query:{},
							out:{ reduce:"comment_sum"},
						}
						)
	}
	