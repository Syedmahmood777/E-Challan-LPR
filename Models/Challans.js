const mongoose=require('mongoose')

const ChallanSchema= new mongoose.Schema({
vehicleno:String,
date:String,
time:String,
pov:String,
cno:String,
violation:String,
fee:Number


})
ChallanSchema.path('_id')

const UserModel=mongoose.model('Challans',ChallanSchema,'Challans')
module.exports=UserModel