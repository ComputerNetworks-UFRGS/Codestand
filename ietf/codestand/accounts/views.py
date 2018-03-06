from ietf.codestand import constants
from django.db.models import Count
from django.http import HttpResponseRedirect, Http404
from ietf.codestand.matches.models import CodingProject, ProjectContainer
from ietf.codestand.helpers.utils import (render_page, get_user)
from ietf.person.models import Person, Email
from django.conf import settings
from ietf.fusioncharts import FusionCharts
from ietf.codestand.helpers.models import Number, StringValue
from ietf.doc.models import DocAlias

def index(request):
    return render_page(request, 'codestand/index.html')


def register(request):
    return HttpResponseRedirect(settings.CODESTAND_PREFIX + '/accounts/create/')


def profile(request, user=None):
    if user is None:
        current_user = get_user(request)
        if current_user is None:
            raise Http404
        else:
            user = current_user.id
    coder = Person.objects.using('datatracker').get(id=user)
    email = Email.objects.using('datatracker').filter(person_id=user)
    projects = ProjectContainer.objects.exclude(code_request__isnull=True).exclude(is_deleted=True).filter(owner=user)
    codings = CodingProject.objects.filter(coder=user)
    all_projects = ProjectContainer.objects.all()
    selected_codings = []
    for proj in all_projects:
        all_codings = proj.codings.all()
        for code in codings:
            if code in all_codings:
                selected_codings.append((proj, code))
    return render_page(request, constants.TEMPLATE_PROFILE, {
        'coder': coder,
        'email': email,
        'projects': projects,
        'codings': selected_codings,
    })


def top_coders(request):
    codings = CodingProject.objects.annotate(count=Count('coder'))
    codes = []
    coders = []
    topcoders = []
    dict_code = {}
    ids = []
    for coding in codings:
        if not coding.is_archived:
            ids.append(coding.coder)
    ids = list(set(ids))
    all_coders = list(Person.objects.using('datatracker').filter(id__in=ids).values_list('id', 'name'))
    for code in codings:
        if code.is_archived:
            continue
        if code.coder not in coders:
            coders.append(code.coder)
            codes.append(code)
            dict_code[code.coder] = code
        else:
            c = dict_code[code.coder]
            c.count += 1
    codes = sorted(codes, key=lambda c: c.count, reverse=True)
    for cd in codes:
        coder = 'None'
        coder_id = 0
        for id, name in all_coders:
            if cd.coder == id:
                coder = name
                coder_id = id
        topcoders.append((cd.count, coder, coder_id))
    return render_page(request, constants.TEMPLATE_TOPCODERS, {
        'topcoders': topcoders,
    })




def countryStatistics():
    aCountryList = []
    aCountryList.append('Afghanistan')
    aCountryList.append('Albania')
    aCountryList.append('Algeria')
    aCountryList.append('Andorra')
    aCountryList.append('Angola')
    aCountryList.append('Antigua and Barbuda')
    aCountryList.append('Argentina')
    aCountryList.append('Armenia')
    aCountryList.append('Australia')
    aCountryList.append('Austria')
    aCountryList.append('Azerbaijan')
    aCountryList.append('Bahamas')
    aCountryList.append('Bahrain')
    aCountryList.append('Bangladesh')
    aCountryList.append('Barbados')
    aCountryList.append('Belarus')
    aCountryList.append('Belgium')
    aCountryList.append('Belize')
    aCountryList.append('Benin')
    aCountryList.append('Bhutan')
    aCountryList.append('Bolivia')
    aCountryList.append('Bosnia and Herzegovina')
    aCountryList.append('Botswana')
    aCountryList.append('Brazil')
    aCountryList.append('Brunei')
    aCountryList.append('Bulgaria')
    aCountryList.append('Burkina Faso')
    aCountryList.append('Burundi')
    aCountryList.append('Cabo Verde')
    aCountryList.append('Cambodia')
    aCountryList.append('Cameroon')
    aCountryList.append('Canada')
    aCountryList.append('Central African Republic')
    aCountryList.append('Chad')
    aCountryList.append('Chile')
    aCountryList.append('China')
    aCountryList.append('Colombia')
    aCountryList.append('Comoros')
    aCountryList.append('Democratic Republic of the Congo')
    aCountryList.append('Republic of the Congo')
    aCountryList.append('Costa Rica')
    aCountryList.append('Croatia')
    aCountryList.append('Cuba')
    aCountryList.append('Cyprus')
    aCountryList.append('Czech Republic')
    aCountryList.append('Denmark')
    aCountryList.append('Djibouti')
    aCountryList.append('Dominica')
    aCountryList.append('Dominican Republic')
    aCountryList.append('Ecuador')
    aCountryList.append('Egypt')
    aCountryList.append('El Salvador')
    aCountryList.append('Equatorial Guinea')
    aCountryList.append('Eritrea')
    aCountryList.append('Estonia')
    aCountryList.append('Ethiopia')
    aCountryList.append('Fiji')
    aCountryList.append('Finland')
    aCountryList.append('France')
    aCountryList.append('Gabon')
    aCountryList.append('Gambia')
    aCountryList.append('Georgia')
    aCountryList.append('Germany')
    aCountryList.append('Ghana')
    aCountryList.append('Greece')
    aCountryList.append('Grenada')
    aCountryList.append('Guatemala')
    aCountryList.append('Guinea')
    aCountryList.append('Guinea-Bissau')
    aCountryList.append('Guyana')
    aCountryList.append('Haiti')
    aCountryList.append('Honduras')
    aCountryList.append('Hungary')
    aCountryList.append('Iceland')
    aCountryList.append('India')
    aCountryList.append('Indonesia')
    aCountryList.append('Iran')
    aCountryList.append('Iraq')
    aCountryList.append('Ireland')
    aCountryList.append('Israel')
    aCountryList.append('Italy')
    aCountryList.append('Jamaica')
    aCountryList.append('Japan')
    aCountryList.append('Jordan')
    aCountryList.append('Kazakhstan')
    aCountryList.append('Kenya')
    aCountryList.append('Kiribati')
    aCountryList.append('Kosovo')
    aCountryList.append('Kuwait')
    aCountryList.append('Kyrgyzstan')
    aCountryList.append('Laos')
    aCountryList.append('Latvia')
    aCountryList.append('Lebanon')
    aCountryList.append('Lesotho')
    aCountryList.append('Liberia')
    aCountryList.append('Libya')
    aCountryList.append('Liechtenstein')
    aCountryList.append('Lithuania')
    aCountryList.append('Luxembourg')
    aCountryList.append('Macedonia')
    aCountryList.append('Madagascar')
    aCountryList.append('Malawi')
    aCountryList.append('Malaysia')
    aCountryList.append('Maldives')
    aCountryList.append('Mali')
    aCountryList.append('Malta')
    aCountryList.append('Marshall Islands')
    aCountryList.append('Mauritania')
    aCountryList.append('Mauritius')
    aCountryList.append('Mexico')
    aCountryList.append('Micronesia')
    aCountryList.append('Moldova')
    aCountryList.append('Monaco')
    aCountryList.append('Mongolia')
    aCountryList.append('Montenegro')
    aCountryList.append('Morocco')
    aCountryList.append('Mozambique')
    aCountryList.append('Myanmar')
    aCountryList.append('Namibia')
    aCountryList.append('Nauru')
    aCountryList.append('Nepal')
    aCountryList.append('Netherlands')
    aCountryList.append('New Zealand')
    aCountryList.append('Nicaragua')
    aCountryList.append('Niger')
    aCountryList.append('Nigeria')
    aCountryList.append('North Korea')
    aCountryList.append('Norway')
    aCountryList.append('Oman')
    aCountryList.append('Pakistan')
    aCountryList.append('Palau')
    aCountryList.append('Palestine')
    aCountryList.append('Panama')
    aCountryList.append('Papua New Guinea')
    aCountryList.append('Paraguay')
    aCountryList.append('Peru')
    aCountryList.append('Philippines')
    aCountryList.append('Poland')
    aCountryList.append('Portugal')
    aCountryList.append('Qatar')
    aCountryList.append('Romania')
    aCountryList.append('Russia')
    aCountryList.append('Rwanda')
    aCountryList.append('Saint Kitts and Nevis')
    aCountryList.append('Saint Lucia')
    aCountryList.append('Saint Vincent and the Grenadines')
    aCountryList.append('Samoa')
    aCountryList.append('San Marino')
    aCountryList.append('Sao Tome and Principe')
    aCountryList.append('Saudi Arabia')
    aCountryList.append('Senegal')
    aCountryList.append('Serbia')
    aCountryList.append('Seychelles')
    aCountryList.append('Sierra Leone')
    aCountryList.append('Singapore')
    aCountryList.append('Slovakia')
    aCountryList.append('Slovenia')
    aCountryList.append('Solomon Islands')
    aCountryList.append('Somalia')
    aCountryList.append('South Africa')
    aCountryList.append('South Korea')
    aCountryList.append('South Sudan')
    aCountryList.append('Spain')
    aCountryList.append('Sri Lanka')
    aCountryList.append('Sudan')
    aCountryList.append('Suriname')
    aCountryList.append('Swaziland')
    aCountryList.append('Sweden')
    aCountryList.append('Switzerland')
    aCountryList.append('Syria')
    aCountryList.append('Taiwan')
    aCountryList.append('Tajikistan')
    aCountryList.append('Tanzania')
    aCountryList.append('Thailand')
    aCountryList.append('Timor-Leste')
    aCountryList.append('Togo')
    aCountryList.append('Tonga')
    aCountryList.append('Trinidad and Tobago')
    aCountryList.append('Tunisia')
    aCountryList.append('Turkey')
    aCountryList.append('Turkmenistan')
    aCountryList.append('Tuvalu')
    aCountryList.append('Uganda')
    aCountryList.append('Ukraine')
    aCountryList.append('United Arab Emirates')
    aCountryList.append('United Kingdom')
    aCountryList.append('United States of America')
    aCountryList.append('United States')
    aCountryList.append('USA')
    aCountryList.append('Uruguay')
    aCountryList.append('Uzbekistan')
    aCountryList.append('Vanuatu')
    aCountryList.append('Vatican City')
    aCountryList.append('Venezuela')
    aCountryList.append('Vietnam')
    aCountryList.append('Yemen')
    aCountryList.append('Zambia')
    aCountryList.append('Zimbabwe')


    aCountryXcoders = []
    nCoderAdressknown = 0

    for oneCountry in aCountryList:
        for n in Number.objects.using('default').raw('''select 1 as id, count(distinct(p.id)) as number
            from person_person p,
            matches_codingproject mc
            where mc.coder=p.id
            and lower(address) like lower(%s) ''', ['%'+oneCountry+'%']):
            if n.number > 0:
                nCoderAdressknown = nCoderAdressknown+n.number
                aCountryXcoders.append([oneCountry, str(n.number)])

    #unknow           
    for n in Number.objects.using('default').raw('''select 1 as id, count(distinct(p.id)) as number
            from person_person p,
            matches_codingproject mc
            where mc.coder=p.id '''):
           
            aCountryXcoders.append(['Unknow', str(n.number-nCoderAdressknown)])              


    return aCountryXcoders


def areaProjects():
  
    all_projects = ProjectContainer.objects.all()
   
    keys = []
    for project_container in all_projects:
        if project_container.docs:
            keys += filter(None, project_container.docs.split(';'))
    keys = list(set(keys))
    all_documents = list(
        DocAlias.objects.using('datatracker').filter(name__in=keys).values_list('name', 'document__group__name',
                                                                                'document__group__parent__name'))
    docs = []
    areas_list = []
    working_groups_list = []
    for project_container in all_projects:
        areas = []
        working_groups = []
        # According to model areas and working groups should come from documents
        keys = []
        documents = []
        if project_container.docs:
            keys = filter(None, project_container.docs.split(';'))
        for key in keys:
            for name, gname, gparentname in all_documents:
                if name == key:
                    documents.append((gname, gparentname))
        for gname, gparentname in documents:
            if gname not in working_groups:
                working_groups.append(gname)
            if gparentname:
                if gparentname not in areas:
                    areas.append(gparentname)
            else:
                if gname not in areas:
                    areas.append(gname)
        #if not areas:
            #areas = [constants.STRING_NONE]
        #if not working_groups:
            #working_groups = [constants.STRING_NONE]
        areas_list.append(areas)
        working_groups_list.append(working_groups)

    areaResult = []
    areaResultXTimes = []
    for oneArea in areas_list:
        if oneArea != []: 
            #print(oneArea[0])
            if oneArea[0] not in areaResult:
                areaResult.append(oneArea[0])
                areaResultXTimes.append([oneArea[0], 1])
            else:
                i = areaResult.index(oneArea[0])                
                areaResultXTimes[i][1] = areaResultXTimes[i][1]+1

    return areaResultXTimes  


def workingGroupProjects():
  
    all_projects = ProjectContainer.objects.all()

   
    keys = []
    for project_container in all_projects:
        if project_container.docs:
            keys += filter(None, project_container.docs.split(';'))
    keys = list(set(keys))
    all_documents = list(
        DocAlias.objects.using('datatracker').filter(name__in=keys).values_list('name', 'document__group__name',
                                                                                'document__group__parent__name'))
    docs = []
    areas_list = []
    working_groups_list = []
    for project_container in all_projects:
        areas = []
        working_groups = []
        # According to model areas and working groups should come from documents
        keys = []
        documents = []
        if project_container.docs:
            keys = filter(None, project_container.docs.split(';'))
        for key in keys:
            for name, gname, gparentname in all_documents:
                if name == key:
                    documents.append((gname, gparentname))
        for gname, gparentname in documents:
            if gname not in working_groups:
                working_groups.append(gname)
            if gparentname:
                if gparentname not in areas:
                    areas.append(gparentname)
            else:
                if gname not in areas:
                    areas.append(gname)
        #if not areas:
            #areas = [constants.STRING_NONE]
        #if not working_groups:
            #working_groups = [constants.STRING_NONE]
        areas_list.append(areas)
        working_groups_list.append(working_groups)

    wgResult = []
    wgResultXTimes = []
    for oneWG in working_groups_list:
        if oneWG != []: 
            print(oneWG[0])
            if oneWG[0] not in wgResult:
                wgResult.append(oneWG[0])
                wgResultXTimes.append([oneWG[0], 1])
            else:
                i = wgResult.index(oneWG[0])                
                wgResultXTimes[i][1] = wgResultXTimes[i][1]+1

    return wgResultXTimes  


def reposStatistics():
    aRepo = []
    aRepo.append('Dropbox')
    aRepo.append('Github')
  
    aReposXcoders = []
    nCoderReposknown = 0

    for oneRepo in aRepo:
        for n in Number.objects.using('default').raw('''select 1 as id, count(1) as number
            from matches_codingproject_links mcl,
            matches_implementation mi
            where mcl.implementation_id=mi.id
            and lower(mi.link) like lower(%s) ''', ['%'+oneRepo+'%']):

            if n.number > 0:
                nCoderReposknown = nCoderReposknown+n.number
                aReposXcoders.append([oneRepo, str(n.number)])

    #unknow           
    for n in Number.objects.using('default').raw('''select 1 as id, count(1) as number
            from matches_codingproject_links mcl,
            matches_implementation mi
            where mcl.implementation_id=mi.id '''):
           
            aReposXcoders.append(['Unknow', str(n.number-nCoderReposknown)])              


    return aReposXcoders


def statistics(request, number):
  
  if number == '1':
    return statistics1(request)
  elif number == '2':
    return statistics2(request)
  elif number == '3':
    return statistics3(request)
  elif number == '4':
    return statistics4(request)    

def statistics1(request):
    aCountrStat = countryStatistics()
    
    chart=  '''{  
        "chart": {
            "caption": "Coders Location",
            "subCaption": "",
            "xAxisName": "Country",
            "yAxisName": "Coders",
            "numberPrefix": "",
            "theme": "zune"
        },
        "data": ['''
    i = 0
    for aCS in aCountrStat:
        i = i+1
        chart=chart+''' {"label": "'''+aCS[0]+'''","value": "'''+aCS[1]+'''"}'''

        if i < len(aCountrStat):
            chart=chart+''','''
        
    chart=chart+''']}'''
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json", chart)
    

    return render_page(request, constants.TEMPLATE_STATISTICS, {'output': column2d.render()})


def statistics2(request):
    aRS = reposStatistics()
    
    chart=  '''{  
        "chart": {
            "caption": "Repositories",
            "subCaption": "",
            "xAxisName": "",
            "yAxisName": "",
            "numberPrefix": "",
            "theme": "zune"
        },
        "data": ['''
    i = 0
    for a in aRS:
        i = i+1
        chart=chart+''' {"label": "'''+a[0]+'''","value": "'''+a[1]+'''"}'''

        if i < len(aRS):
            chart=chart+''','''
        
    chart=chart+''']}'''
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json", chart)
    

    return render_page(request, constants.TEMPLATE_STATISTICS, {'output': column2d.render()})

def statistics3(request):
    area = areaProjects()
    
    chart=  '''{  
        "chart": {
            "caption": "Project Areas",
            "subCaption": "",
            "xAxisName": "",
            "yAxisName": "",
            "numberPrefix": "",
            "theme": "zune"
        },
        "data": ['''
    i = 0
    for a in area:
        i = i+1
        chart=chart+''' {"label": "'''+a[0]+'''","value": "'''+str(a[1])+'''"}'''

        if i < len(area):
            chart=chart+''','''
        
    chart=chart+''']}'''
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json", chart)
    

    return render_page(request, constants.TEMPLATE_STATISTICS, {'output': column2d.render()})

def statistics4(request):
    wg = workingGroupProjects()
    
    chart=  '''{  
        "chart": {
            "caption": "Project Working Groups",
            "subCaption": "",
            "xAxisName": "",
            "yAxisName": "",
            "numberPrefix": "",
            "theme": "zune"
        },
        "data": ['''
    i = 0
    for w in wg:
        i = i+1
        chart=chart+''' {"label": "'''+w[0]+'''","value": "'''+str(w[1])+'''"}'''

        if i < len(wg):
            chart=chart+''','''
        
    chart=chart+''']}'''
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json", chart)
    

    return render_page(request, constants.TEMPLATE_STATISTICS, {'output': column2d.render()})