# - Coding UTF8 -
#
# Networked Decision Making
# Development Sites (source code): http://github.com/DonaldMcC/gdms
#
# Demo Sites (Pythonanywhere)
#   http://netdecisionmaking.com/nds/
#   http://netdecisionmaking.com/gdmsdemo/
#
# License Code: MIT
# License Content: Creative Commons Attribution 3.0
#
# Also visit: www.web2py.com
# or Groups: http://groups.google.com/group/web2py
# For details on the web framework used for this development
#
# With thanks to Guido, Massimo and many other that make this sort of thing
# much easier than it used to be

# This controller has 3 functions:
# my_questions for reviewing progress on questions you have asked
# my_answers for reviewing your answers
# resovled for reviewing resolved questio

"""This controller has 3 functiosns:
index: -        simple listing of all locations now with buttons
new_project -  for creating and shortly editing locations
my_locations -  for creating, updating and deleting details of your locations perhaps duplicated
                with new_location 
locations       for seeing a list of locations that are setup
viewlocation -  for reviewing details of a single location and links to the events that
                are planned to take place there
"""


@auth.requires(True, requires_login=requires_login)
def index():
    page = request.args(0, cast=int, default=0)
    items_per_page = 20
    limitby = (page * items_per_page, (page + 1) * items_per_page + 1)
    projects = db(db.project.id > 0).select(orderby=[~db.project.createdate], limitby=limitby)
    return dict(projects=projects, page=page, items_per_page=items_per_page)


    
    db.define_table('project',
                Field('proj_name', label='Event Name'),
                Field('proj_url', label='Project Website'),
                Field('pro_status', 'string', default='Open',
                      requires=IS_IN_SET(['Open', 'Archiving', 'Archived'])),
                Field('answer_group', 'string', default='Unspecified', label='Restrict Project to Group'),
                Field('startdatetime', 'datetime', label='Start Date Time',
                      default=(request.utcnow), widget=bsdatetimepicker_widget()),
                Field('enddatetime', 'datetime', label='End Date Time',
                      default=(request.utcnow + datetime.timedelta(days=365)), widget=bsdatetimepicker_widget()),
                Field('description', 'text'),
                Field('proj_shared', 'boolean', default=False, label='Shared Event', comment='Allows other users to link questions'),
                Field('proj_owner', 'reference auth_user', writable=False, readable=False, default=auth.user_id,
                      label='Owner'),
                Field('createdate', 'datetime', default=request.utcnow, writable=False, readable=False),
                format='%(proj_name)s')
                
@auth.requires_login()
def new_project():
    # This allows creation and editing of a locations by their owner
    fields = ['proj_name', 'description', 'proj_url', 'answer_group', 'startdatetime', 'enddatetime', 'proj_shared']
    projid = request.args(0, default=None)
    if projid is not None:
        record = db.project(projid)
        if record.auth_userid != auth.user.id:
            session.flash = 'Not Authorised - projects can only be edited by their owners'
            redirect(URL('new_project'))
        form = SQLFORM(db.project, record, fields=fields)
    else:
        form = SQLFORM(db.project, fields=fields)

    if form.validate():
        if projid:
            if form.deleted:
                db(db.project.id == projid).delete()
                response.flash = 'Project deleted'
                redirect(URL('default', 'index'))
            else:
                record.update_record(**dict(form.vars))
                response.flash = 'Project updated'
                redirect(URL('default', 'index'))
        else:
            form.vars.id = db.project.insert(**dict(form.vars))
            session.flash = 'Project Created'
            redirect(URL('accept_project', args=[form.vars.id]))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires(True, requires_login=requires_login)
def accept_project():
    response.flash = "Location Created"
    return locals()


@auth.requires_login()
def my_projects():
    # thinking is users shouldn't have that many of these so this should be easy - will need to be a button
    # to view events at this location and that this shold list all locations
    # but not sure that this is any better than just a simple query on location\index - to be considered
    query1 = db.locn.auth_userid == auth.user.id
    myfilter = dict(project=query1)
    grid = SQLFORM.smartgrid(db.project, constraints=myfilter, searchable=False)
    return locals()


@auth.requires(True, requires_login=requires_login)
def viewproject():
    projid = request.args(0, cast=int, default=0) or redirect(URL('index'))
    projectrow = db(db.proj.id == projid).select().first()
    return dict(projectrow=projectrow, projid=projid)