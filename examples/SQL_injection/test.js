app.get("/get-info", (request, response) => {
const req=request.query
const query="SELECT * FROM contact_list where id="+req.id;
connection.query(query,(err,rows) => {
  if(err) throw err;

  response.json(rows)

});
})
connection.query("select * FROM bank_accounts where dob = '" + req.body.dob + " AND bank_account = " + req.body.account_number + "'",
    function(error, results) {

    }
);