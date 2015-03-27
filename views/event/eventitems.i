<div id="target"></div>

<h1>Issues for event</h1>
<div id="issueprog">
{{=LOAD('default','questload.load',args=['evtunlink','Issue'],vars=dict(selection='IP'), event=eventid, ajax=True,target="issueprog")}}
</div>



<h1>Questions for event</h1>
<div id="questprog">
    <script>
$("#questprog").load("{{=URL('default', 'questload.load', args='evtunlink', vars=dict(selection='QP',event=eventid, items_per_page=50, sortby='ResDate'))}}","test", function() {
  $('#QP').DataTable();} );
</script>

</div>


<h1>Proposed Actions from event</h1>
<div id="actionprog">
    <script>
$( "#actionprog" ).load("{{=URL('default', 'questload.load', args=['evtunlink'],vars=dict(selection='AP', event=eventid, items_per_page=50, query='home', sortby='ResDate'))}}","test", function() {
  $('#AP').DataTable();} );
</script>
</div>


<h1>Already Resolved Issues</h1>
<div id="issueresolved">
{{=LOAD('default','questload.load',args=['evtunlink','Issue'],vars=dict(selection='IP',event=eventid), ajax=True,target="issueresolved")}}
</div>


<h1>Already Resolved Questions</h1>
<div id="questresolved">
    <script>
$( "#questresolved" ).load("{{=URL('default', 'questload.load', args=['evtunlink'], vars=dict(selection='QR', event=eventid, items_per_page=50,sortby='ResDate'))}}","test", function() {
  $('#QR').DataTable();} );
</script>
</div>


<h1>Already Agreed Actions</h1>
<div id="actionresolved">
    <script>
$( "#actionresolved" ).load("{{=URL('default', 'questload.load', args=['evtunlink'],vars=dict(selection='AR', event=eventid, items_per_page=50, query='home', sortby='ResDate'))}}","test", function() {
  $('#AR').DataTable();} );
</script>
</div>