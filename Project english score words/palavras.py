palavras = """
Appliance = utensílio
Ash = cinzas
Awareness = conhecimento
Ackowledge = reconhecer
Arid = árido(a)
Automakers = montadoras
Aircraft = aeronave
Affordable = acessível
Appeals = apelações
Anthem = hino
Abseil = rapel
Argument = argumento / discussão
Amid = em meio a
Alas / unfortunately = infelizmente
Aimed = destinado(a)
Amazement = espanto
Alley = beco
Afford = proporcionar / dispor
Aggrieved = magoado(a)
Attend = comparecer
Amounts = quantidades
Airbrushes = aerógrafos(as)
Absence = ausência
Appointment = compromisso
Aims = mira
Arose = surgiu
Aid = ajudar / auxiliar / acudir
Appetizer = aperitivo / a entrada / o antepasto
Adrift = à deriva / à toa
Airlifted = transportados por via aérea
Aging = envelhecimento
Archway = arco
Armchair = poltrona / braço de cadeira
Antiqueness = antiguidade / velharia
Antlers = galhada
Acquaintance = conhecido(a)
Amend = alterar / emendar / corrigir / reformar / melhorar / aperfeiçoar
Allegiance = fidelidade / submissão / obediência
Amendments = emendas
Aim = mirar / alvo / objetivo
Allergy = alergia
Aftershocks = tremores secundários
Assault = assalto / ataque / investida
Ambusher = emboscador
Assemble = montar / reunir / juntar / convocar / agregar
Attempting = tentando
Afterwards = depois / mais tarde
Aid = ajuda
Abroad = fora do país / no exterior
All-encompassing = abrangente
Abducted = raptado(a)
Amiable = amável
Adorable = adorável
Application = inscrição / pedido
Ace = ás
Accountant = contador(a)
AM = indica o período que vai da meia-noite até as 11:59 da manhã.
Arrow = seta /
Attach = anexar
Attempted coup = tentativa de golpe
Affordability = acessibilidade
Amusement = diversão
Assessment = avaliação
Asylum = asilo / hospício / refúgio
Around the clock = o tempo todo
Appraisal = avaliação
Auction = leilão
Airborne = transportado por vias áreas / no ar / transportado pelo ar
Aiming = visando
Ape = macaco
"""

linhas = palavras.strip().split('\n')
# print(linhas)

ingles_A = []
portugues_A = []

for linha in linhas:
    ingles_A.append(linha.split(' = ')[0])
    portugues_A.append(linha.split(' = ')[1])
# print(ingles_A)
# print(portugues_A)

palavras2 = """
Bespoke = sob medida
Bark = latido
Bore = calibre
Bluff = blefe
Brother in law = cunhado
Booming = estrondoso(a)
Blood flow = fluxo sanguíneo
Beverages = bebidas
Blankets = cobertores
Bubble wrap = plástico bolha
Bins = caixas
Beauty pageants = concursos de beleza
Bonnets = gorros
Beneath = abaixo
Barking = latidos
Blaring = estridente
Bleating = balido(a)
Benchmark = referência
Bank = banco / margem(rio,lago...)
Being ill = estar doente
Bottom = inferior
Briefed = informado(a)
Broomstick = cabo de vassoura
Broom = vassoura
Birds of prey = aves de rapina
Bylaws = estatutos
Befall = acontecer
Blimey = caramba
Backfired = saiu pela culatra
Brash = impetuosa(o)
Boast = vangloriar-se
Besmirching = manchando
Border = fronteira
Briefly = brevemente
Breached = violado(a)
Bend = dobrar / curvar / torcer
Blab = tagarelar
Blabbering = tagarelando
Backwards = para trás
Breastfed = amamentado(a)
Baseless = sem fundamento / infundado
Brewing = fermentação / preparação
Boggled = confuso(a)
Blockbuster  = sucesso de bilheteria
Begrudge = invenjar / dar de má vontade
Blindfold = de olhos vendados
Beehives = colmeias
Beekeepers = apicultores(as)
Bloodlust = sede de sangue
Brew = preparar / fermentação / bebiba fermentada / infusão
Burrow = toca / cova / refúgio
Bequest = legado / herança / doação
By all means = por todos os meios / certamente / de todo jeito
Banging = batendo
Bragged = gabar-se / vangloriar-se
Brakes = freios
Binding = vinculativo / ligação / amarração
Bill = conta
Blanket = cobertor / manta / coberta
Bankrupt = falido(a) / quebrado / arruinado
Brightens = ilumina 
Bloopers = erros de gravação
Believers = crentes
Bodyguards = guarda-costas
Beliefs = crenças
Beetles = besouros
Bliss = felicidade
Blossom = florescer
Bankrupt = falido(a) / quebrado(a) / arruinado(a)
Bankruptcy = falência
Breakthrough = avanço
Briefly = brevemente
Bomb shelter = abrigo de bomba
Brief = breve / sumário / curto 
Bustling = movimentado(a) / agitado / barulhento 
Big bands of colors = grandes faixas de cores
Begone = ir embora
Bickering = brigar / questionar / murmurar
Brewery = cervejaria
Bake = assar / cozer no forno / queimar
Bind = ligar / vincular / prender / amarrar
Bonfire = fogueira
Busy highway = estrada movimentada
Back door = porta dos fundos
Breeders = criadores
Broad daylight = em plena luz do dia
Bogged down = atolado
Badly = seriamente
Bringer = portador(a)
Blunt = cego / brusco
Bolt = parafuso
Bash = festança
Bore = calibre / diâmetro
Ballooned = inflado(a)
Breathtaking = tirar o fôlego / empolgante
Basin = bacia / recipiente
Bidder = licitante
Bystanders = Espectadores(as)
Breadth = largura
Bedlam = tumulto
"""

linhas2 = palavras2.strip().split('\n')
# print(linhas2)

ingles_B = []
portugues_B = []

for linha in linhas2:
    ingles_B.append(linha.split(' = ')[0])
    portugues_B.append(linha.split(' = ')[1])
# print(ingles_B)
# print(portugues_B)

palavras3 = """
Cub = filhote
Crept = rastejou
Crawled = rastreado(a)
Came up = apareceu
Commuters = passageiros(as)
Convoy = comboio
Crackdown = repressão
Crystalline = cristalino
Crystal clear = cristalina
Cans = latas
Creepy crawlies = bichos rastejantes
Crop = colheita
Ciders = sidras
Chin = queixo
Clamp = grampo
Childbirth = parto
Crowd = multidão
Cucumber = pepino
Crackling = crepitante
Concern = preocupação
Cable car = bonde / bondinho
Crude = bruto(a)
Carrier = portador
Censorship = censura
Content = conteúdo
Chok = engasgar
Chew = mastigar / mascar
Customers = clientes
Cabbages = repolhos
Cupboard = armário
Culprit = culpado(a)
Conveyor belt = correia transportadora
Chopped vegetables = legumes picados
Caretaker = zelador(a)
Cozy = aconchegante
Combed = penteado
Cast them away = jogue-os fora
Canopy = marquise
Cattle = gado
Comprised = composto(a)
Concerned = preocupado(a)
Cocky = pretencioso(a) / convencido(a)
Cargo ship = cargueiro
Capsizing = virando
Crops = plantações
Clattering = barulhento(a)
Cane = bengala
Concoctions = misturas
Chitchat = bate papo / tagarelice / fofoca
Coax = persuadir / aliciar / influenciar
Crest = crista / cume
Crowded = lotado(a) / superlotado(a)
Canister = vasilha
Creepy = repugnante / rastejante / arrepiante
Concerns = preocupações
Core = núcleo / testemunho / cerne
Clatter = barulho / ruído / algazarra
Cage = cela / jaula / caixa / gaiola
Craved = ansiava / desejar / implorar / almejar / suplicar
Cunning = ardiloso(a) / habilidade / capacidade / astúcia
Conveyed = transmitido(a)
Concealed = escondido(a)
Chopsticks = pauzinhos
Crummy = miserável / sujo / rico
Clobber = espancar
Condiment / flavoring / seasoning = condimento
Courtroom = tribunal
Crop grower = agricultor
Crossroads = encruzilhada / cruzamento
Centuries old = séculos de idade
Crane = guindaste
Coal = carvão
Carving  = esculpir / talha / gravura / escultura
Clipper = tosquiadeira / cortador
Cautious = cauteloso(a)
Chaperone = acompanhante / a dama de companhia
Compelling = convincente
Chilling = arrepiante
Cherished = acarinhado
Clutches = garras
Complained = reclamou
Capped = tampado(a)
Copper = cobre
Can = posso / lata / recipiente / vasilha
Comb = pente
Constrict = comprimir / apertar / contrair
Crunchy = crocante
Costly = dispendioso(a)
Coincidentally = coincidentemente
Curtain = cortina
Casualties = baixas
Coastline = litoral
Caterwaul = lagarta / miado 
Cipher = cifra / criptograma
Conceit = presunção / vaidade
County = município / condado
Chimp = chimpanzé
Coverage = cobertura
Contagion = contágio
Ceiling = teto
Comforter = edredom
Calves = bezerros(as)
Clothing = confecções / vestuário / roupa
Cross-border bridge = ponte transfronteiriço
Cluster = conjunto
Crammed = abarrotado(a)
Curating = curadoria
Catch up on = colocar em dia
Crates = caixotes
Commonwealth = comunidade
Conceals = esconde
"""

linhas3 = palavras3.strip().split('\n')
# print(linhas3)

ingles_C = []
portugues_C = []

for linha in linhas3:
    ingles_C.append(linha.split(' = ')[0])
    portugues_C.append(linha.split(' = ')[1])
# print(ingles_C)
# print(portugues_C)


palavras4 = """
Diverting = desvio
Disrupted = interrompida(a)
Discared = descartado(a)
Dismantle = desmantelar
Daylight saving time = horário de verão
Due to = devido a
Death threats = ameaças de morte
Dizziness = tontura
Displace = deslocar
Demanding = exigente
Dishes = pratos
Dumped = despejado(a)
Deaf = surdo(a)
Detours = desvios
Dam(s) = barragem(s)
Drought = seca
Default = predefinição
Dairy = laticínios
Drags = arrasta
Downfalls = quedas
Dodgy = desonesta(o)
Dozed off = cochilou
Defiant = desafiador(a)
Dwindling = diminuindo
Donors = doadores(as)
Dimwitted = estúpido(a)
Dashing = arrojado(a) / impetuoso / fogoso
Doorway = o vão da porta / entrada
Data breaches = violação de dados
Duty = dever / a obrigação / o imposto
Disorder = transtorno
Distress call = pedido de ajuda
Deck = área coberta / convés
Disability = incapacidade / inaptidão / inabilidade 
Depicting = representando / retratar / descrever
Defy = desafiar / resistir / provocar
Discard = descartar / rejeitar / desfazer-se
Daft = idiota / maluco / tolo
Deed = ato
Daresay = ouso dizer
Delighted = encantado(a) / satisfeito(a)
Dessert = sobremesa
Dreadful = terrível / medonho / espantoso
Doomed = condenado(a)
Dawdling = demorando / perder o tempo
Dealer = distribuidor(a)
Deceased = morto(a) / falecido(a)
Dearie = querida(o)
Downfall = queda / ruina / perdição
Divination  = adivinhação / palpite
Dizzying = vertiginoso(a) / entontecer / confundir / atordoar
Defrauded = fraudado(a)
Dozens = dezenas
Depth = profundidade
Dismay = desânimo
Doomed = condenado(a)
Dump = jogar fora / despejar / descarregar / esvaziar
During / for / over = durante
Downpour = aguaceira
Den = covil
Dull = maçante
Deadly = mortal
Duo = dupla 
Desolate = desolado
Deafening = ensurdecedor
Destitute = destituído / necessitado / desprovido / indigente
Distraught = atormentado
Docked = ancorado(a)
Depleted = esgotado(a)
Dreary = aborrecido(a)
Drawer = gaveta / sacador
Delayed = atrasado(a)
Dropout = cair fora
Double-track = via dupla
Deploys = implanta
Diverted = desviado(a)
Debris = destroços / detritos / restos
Diversion = desvio / diversão / distração
Deterrent = dissuasão / o meio de intimidação / dificuldade
Donning = vestindo
Dizzy = tonto(a) / atordoado
Depiction = representação
Drip = gotejamento
Dubbed = apelidado(a)
Disposal = disposição
Duped = enganado(a)
Dissent = dissidência / divergência
Displaced = deslocado(a)
Deemed = considerado(a)
Depths = profundidades
Deity = divindade
Dognapper = ladrão de cães
Distress = sofrimento / aflição
Droves = multidões
Depicts = retrara
"""

linhas4 = palavras4.strip().split('\n')
# print(linhas4)

ingles_D = []
portugues_D = []

for linha in linhas4:
    ingles_D.append(linha.split(' = ')[0])
    portugues_D.append(linha.split(' = ')[1])
# print(ingles_D)
# print(portugues_D)

palavras5 = """
Endangered = ameaçadas de extinção
Embedded = embutido
Endurance = resistência
Enshrined = consagrado(a)
Engulfed = engolido(a)
Essay = redação
Erode = corroer
Encirded = cercado
Enclosure = recinto / invólucro
Earwax = cera de ouvido
Elbow = cotovelo
Eastern  = oriental
Efforts = esforços
Establish = estabelecer / consagrar
Envisage = imaginar / encarar / enfrentar
Eponymous = epônimo
Encompassed = englobado(a)
Erected = erigido(a)
Engine = motor
Exceedingly = extremamente
Endeavor = empenho / esforço / tentativa
Exploiting = explorando
Enhance = realçar / aumentar / elevar
Eager = ansioso(a) / impaciente 
Ensure = garantir
Elderly = idoso(a)
Engaged = acionado(a)
Enhancing = aprimoramento
Etches = grava / causticar / cauterizar
Eddy = redemoinho
Effortless = sem esforço / fácil / passivo
Extensive = vasto / extenso
Exact = exato / preciso / justo
Ecstatic = em êxtase 
Exhilarating = emocionante  
Exposure = exposição
Embodiment = encarnação
Elsewhere = em outro lugar
Emblazoned = brasonado
Easing = flexibilização 
Embers = brasas
Enrolled = matriculado(a) 
Engage = se empenhar / engajar / engatar
Encampment = acampamento
Exemption = isenção
Edible = comestível
Evaluated = avaliado(a)
Embassy = embaixada
"""

linhas5 = palavras5.strip().split('\n')
# print(linhas5)

ingles_E = []
portugues_E = []

for linha in linhas5:
    ingles_E.append(linha.split(' = ')[0])
    portugues_E.append(linha.split(' = ')[1])
# print(ingles_E)
# print(portugues_E)


palavras6 = """
Famine = fome
Frightened = assustado(a) / amendrontado
Fine = multar
Finnish = finlandês/finlandesa
Float = flutuador(a)
Franchise = franquia
Floods = inundações
Fulfill = preencha
Forecasts = previsões
Flies = mosquitos / moscas
Facilities = instalações
Figure skater = patinadora
Flock = rebanho
Fowl = galinha
Ferry = balsa
Felon = criminoso
Fleas = pulgas
Frightening footage = imagens assustadoras
Fined = multado(a)
Falling short = ficando aquém
Flouted = desprezado(a)
Foulest = mais sujo
Filthy = imundo(a) / sujo / obsceno
Fret = irritar
Fitting = apropriado(a)
Fastidious = exigente
Fair-minded = justo(a)
Fledgling = novato(a)
Feed truck = caminhão de alimentação
Fences = cercas
Flattened = achatado(a)
Faint-hearted = desanimado(a) / covarde / medroso / tímido
Fiance / bride = noiva
Fetch = buscar / trazer 
Forbade = proibido(a)
First off = primeiramente
Filmmakers = cineastas
Flicked = sacudiu / agitar / esvoaçar / chicotear levemente
Fancy = extravagante / imaginário / invulgar
Flapping = batendo / agitar / vibrar
Fortune teller = vidente
Flippant = irreverente / superficial / desenvolto
Forbids = proíbe
Flanker = flanqueador
Freehand  = à mão livre / sagacidade / reserva / prudência
Fares = tarifas
Fearful = medo / medroso / temeroso / tímido 
Fierce / ferocious = feroz
Freezing = congelando
Forceful = forte / violento
Flawless = sem falhas
Filthy = imundo / sujo / imoral
Frail = frágil
Features = recursos
Flew = voei
Fire crews = equipes de bombeiros
Faucet / tap = torneira
From now on = de agora em diante
Freighter = cargueiro
Flooring = piso / pavimentação / pavimento
Feed source = fonte de alimentação
Footpath = trilha
Forefathers = antepassados
Furious = furioso(a)
Flushers = lavadores
Falsehoods = falsidades
"""

linhas6 = palavras6.strip().split('\n')
# print(linhas6)

ingles_F = []
portugues_F = []

for linha in linhas6:
    ingles_F.append(linha.split(' = ')[0])
    portugues_F.append(linha.split(' = ')[1])
# print(ingles_F)
# print(portugues_F)


palavras7 = """
Gathered = coletado(a) / acumulado
Grabbed = agarrou
Guesses = palpites
Glimpse = vislumbre
Gasps = suspiros
Gasping = ofegante
Greases = graxas
Grasp = aperto / entender / a compreensão
Grew crops = cultivou colheitas
Greeted = saudado(a)
Greetings = saudações
Ghastly = medonho(a) / sinistro
Greenhouses = estufas
Grab = agarrar / apanhar / roubar
Gather = juntar / reunir
Guts = culhões / a coragem / a raça
Groom = noivo
Groaning = gemendo
Gavel = martelo
Giggles = risadinhas
Gargoyle = gárgula
Grunts = grunhidos / gemido / ronco
Granted = garantido(a) / admitido / permitido / reconhecido
Gluten = glúten
Gluten-free = sem glúten
Greeted = saudado(a)
Glaciers = geleiros(as)
Gig = show / apresentação
Gorgeous = lindo(a) / deslumbrante / esplêndido
Gleaming = brilhando / reluzente
Guarantees = garantias
Grocery = mercado / mercearia
Gunmen = pistoleiros
Graduate = formar-se
Grocery store = mercado
Goes off = apaga
Gripped = agarrado(a)
Gravel = cascalho / pedregulho
Grower = produtor(a)
Grim = sinistro(a)
Goods = bens / mercadorias
Grit = grão / ranger
Gouged out = arrancados
Gaggle = bando
"""

linhas7 = palavras7.strip().split('\n')
# print(linhas7)

ingles_G = []
portugues_G = []

for linha in linhas7:
    ingles_G.append(linha.split(' = ')[0])
    portugues_G.append(linha.split(' = ')[1])
# print(ingles_G)
# print(portugues_G)

palavras8 = """
Household = doméstico(a)
Hangings = enforcamentos
Hiring = contratando
Hurdle = obstáculo
Hut = cabana
Has been bashed = foi golpeado
Harmful = prejudicial
Headscarf = lenço de cabeça
Harbor = porto
Homelessness = sem-teto
Houseboat = casa flutuante
Hire = contratar
Hold out = aguentar
Harvested = colhido(a)
Hunch = palpite
Handcuffed = algemado(a)
Handguns = revólveres
Host = anfitrião
Harassment = assédio
Hanging around = andando por aí
Hood = capuz
Hue = matiz
Hook = gancho
Heritage = herança
Hostage = refém
Heir = herdeiro
Hairy = peludo(a)
His final pay slip = sua última folha de pagamento
Humming along to waltz = cantarolando junto a valsa
Hold out your arm = estenda seu braço
Heinous = hediondo(a)
Hurls = lança / arremessa
Hovering = pairando
Herds = rebanhos
Hub = eixo / o cubo / o ponto central
Hoax = farsa / o trote / a brincadeira
Harnessed = aproveitado(a) / arrear / atrelar / couraçar
Halved = metade
Households = famílias
Householders = chefe de família
Hereby = por este meio
Hissing = assobio
Halted = parado(a)
Handy = útil
Hourglass = ampulheta
Handful = punhado(a)
Haul = transporte / arrastar / rebocar
Hereafter = daqui em diante / futuramente
Hike = caminhada / marcha
Homeland = terra natal / pátria
Hatchet = machadinha
Howling = uivando / gritante / barulhento / vociferante
Holey = esburacado(a)
Hooded = encapuzado
Hawthorn = espinheiro
Hideous = medonho(a) / terrível / muito feio
Hometown = cidade natal
Hairdresser = cabeleireiro(a)
Highway = rodovia
Huge = imenso / enorme
Hideous = horrível / muito feio
Hilarious = hilário / divertido 
 High-income = alta renda
Hangs up = trava / desliga
Handicraft = artesanato
Hang = pendurar / enforcar 
Hung = pendurado(a)
Hogs = porcos(as)
Hockey stick = taco de hóquei
Headache = dor de cabeça / enxaqueca
Heatstroke = insolação
Hardened = endurecido(a)
Harsh = severo(a) / áspero / rigoroso
Healthiest = mais saudável
Hurtful = doloroso(a)
Harness = aproveitar
Harassed = assediado(a)
Henceforth = daqui em diante
Hassle = problema
High-rise = arranha-céus
Hefty = robusto(a)
"""

linhas8 = palavras8.strip().split('\n')
# print(linhas8)

ingles_H = []
portugues_H = []

for linha in linhas8:
    ingles_H.append(linha.split(' = ')[0])
    portugues_H.append(linha.split(' = ')[1])
# print(ingles_H)
# print(portugues_H)


palavras9 = """
Innate = inato(a)
Issued = publicado(a)
Inherent = inerente
Income = renda
Inmates = presos(as)
Inequalities = desigualdades
Illness = doença
Inn = pousada / estalagem / hotel
Incontrovertible = incontroverso(a) / incontestável / irrefutável
Ink = tinta
Inspiring = inspirador(a)
Ironbelly = barriga de ferro
Insipid = insosso
Ignite = acender / inflamar / incendiar
Inquiry = investigação / inquérito
Infighting = luta interna
Incoming = entrada
Inner = interior
Indolent = indolente / insensível / preguiçoso
Infants = bebês
Invoice = fatura / conta
Inches = polegadas
Ice-skating rink = pista de patinação de gelo
Insurance = seguro
Insulation = isolamento
Increasingly = cada vez mais / aumentar / de modo crescente
Intake = ingestão
"""

linhas9 = palavras9.strip().split('\n')
# print(linhas9)

ingles_I = []
portugues_I = []

for linha in linhas9:
    ingles_I.append(linha.split(' = ')[0])
    portugues_I.append(linha.split(' = ')[1])
# print(ingles_I)
# print(portugues_I)


palavras10 = """
Jaw = mandíbula
Joints = articulações
Jinx = azar / má sorte
Journeys = viagens
Jackpot = prêmio / bolada
Jaw-dropping = de cair o queixo
"""

linhas10 = palavras10.strip().split('\n')
# print(linhas10)

ingles_J = []
portugues_J = []

for linha in linhas10:
    ingles_J.append(linha.split(' = ')[0])
    portugues_J.append(linha.split(' = ')[1])
# print(ingles_J)
# print(portugues_J)


palavras11 = """
Kindergartens = jardins de infância
Knowingly = sabidamente / conscientemente / intencionalmente
Knowledgeable = bem informado
Keepsake = lembrança / recordação / dádiva
Kitten = gatinho(a)
Keen = interessado / afiado / mordaz
Kettle = chaleira
"""

linhas11 = palavras11.strip().split('\n')
# print(linhas11)

ingles_K = []
portugues_K = []

for linha in linhas11:
    ingles_K.append(linha.split(' = ')[0])
    portugues_K.append(linha.split(' = ')[1])
# print(ingles_K)
# print(portugues_K)


palavras12 = """
Livestock = gado
Lifespan = vida útil
Lungs = pulmões
Lasts longer than = dura mais do que
Leans = inclina-se
Lane = faixa
Landfill = aterro
Lawmakers = legisladores(as)
Laborious = trabalhoso(a)
Lifelong = vitalício(a)
Labelled as flushable = rotulado como lavável
Leaky = com vazamento
Linger = permanecer
Longing = anseio
Loathsome = repugnante
Lingered = demorou
Lifeboats = botes salva-vidas
Lumberjacks = lenhadores
Leap = salto
Loop = ciclo / laço
Lounge = saguão
Lace = renda
Loquacious = falador / tagarela
Lack = a falta / a carência / a necessidade
Lowly = modesto / humilde
Long-term = longo prazo
Laces untied = laços desamarrados
Lobster = lagosta
Limbs = membros
Lofty = sublime / alto / elevado
Lurking = à espreita
Lurk = emboscar / esconder-se
Lettuce = alface
Lanes = pistas
Lift spirits = elevar os ânimos
Lifted = levantado(a)
Likeness = semelhança / imagem / aparência
Locket = medalhão
Latched = travado(a) / trancar
Lure = atrair / seduzir / fascinar / encantar
Lacking = em falta / sem
Lackeys = lacaios
Lactose = lactose
Lactose-intolerance = intolerância à lactose
Ledge = saliência / ressalto / rebordo
Life insurance = seguro de vida
Landscape = panorama / a vista / a paisagem
Lift = levantar / erguer 
Labor = trabalho
Lying = deitado(a)
Low-income workers = trabalhadores de baixa renda
Lavish = luxuoso
Leaden = chumbo / pesado / pesado como chumbo 
Lieutenant = tenent
Layers = camadas
Litters = ninhadas
Loin = lombo
Lipstick = batom
Landfills = aterros sanitários
Lit = aceso(a)
Lounging = descansando
Lieutenant = tenente
Lashed = açoitado(a)
Lorries = caminhões
Least = ao menos / mínimo / menos importante
Luggage = bagagem
Latch = trava
Leaderboard = entre os melhores
Lattes = café com leite
"""

linhas12 = palavras12.strip().split('\n')
# print(linhas12)

ingles_L = []
portugues_L = []

for linha in linhas12:
    ingles_L.append(linha.split(' = ')[0])
    portugues_L.append(linha.split(' = ')[1])
# print(ingles_L)
# print(portugues_L)


palavras13 = """
Mistakenly = erroneamente
Make room = criar espaço
Masts = mastros
Mesmerized = hipnotizado(a)
Maiden name = nome de solteira
Mischievous = pernicioso(a)
Moisture = umidade
Meaningless = sem significado
Meters a long = metros de comprimento
Mistrut = desconfiar
Mauled = ferido(a)
Mild / soft = suave
Maintenance = manutenção
Misuse = uso indevido
Mangled = mutilado(a) / destroçar
Mermaid = sereia
Misfits = desajustados
Maddening = enlouquecedor
Maze = labirinto
Mock-up = brincar / a maquete / o modelo
Melee = corpo a corpo
Misled = enganado(a)
Mumbling = resmungando
Mown = ceifado(a)
Misunderstand = entender mal
Motorway = auto-estrada
Manner = maneiras / modo / espécie
Muffled = abafado(a)
Muttering = murmurando
Menu = cardápio
Mitigating = atenuante / abrandar
Monsoon rains = chuvas de monção
Monk = monge / monja
Melted = derretido(a)
Massive = enorme 
Mountain range = cadeia de montanhas
Membership = filiação
Misjudge = julgar mal
Mouthwash  = enxaguante bucal
Misleading = errôneo(a) / enganosa
Major = principal
Meld = fundir
Moreover = além disso / aliás / além do mais
Maim = mutilar
Meager = escasso(a) / magro / deficiente
Merge = mesclar / fundir / misurar
Mulled = meditado(a) / ponderado / confundido
Model-makers = modelistas
"""

linhas13 = palavras13.strip().split('\n')
# print(linhas13)

ingles_M = []
portugues_M = []

for linha in linhas13:
    ingles_M.append(linha.split(' = ')[0])
    portugues_M.append(linha.split(' = ')[1])
# print(ingles_M)
# print(portugues_M)


palavras14 = """
Nevertheless = no entanto
Nationwide = nacional
Northwards = para o norte
Net profit = lucro líquido
Noxious fume = fumaça nociva
Nuclear power plants = usina nuclear
Not washable = não lavável
Nuns = freiras
Newest = o(a) mais novo(a)
Nuzzing = aninhar-se
Niceties = delicadezas
Northeast = nordeste
Narrow = estreito(a)
Neural pathways = vias neurais
Nutter = maluco(a)
Necklace = colar
Noncompliance = descumprimento
Naive = ingénuo(a)
Not quite = não exatamente
Nursing home = lar de idosos / casa de repouso
Non-stop = sem parada / direto / interrupções
Notepad = bloco de notas
Nods = acena com a cabeça
Nuisance = incômodo(a)
Nonetheless = não obstante
Norse = nórdico / escandinavo / norueguês
Naughty = desobediente / malcriado / perverso
Numbness = dormência
Nobel peace prize = prémio nobel da paz
Nonchalantly = com indiferença
"""

linhas14 = palavras14.strip().split('\n')
# print(linhas14)

ingles_N = []
portugues_N = []

for linha in linhas14:
    ingles_N.append(linha.split(' = ')[0])
    portugues_N.append(linha.split(' = ')[1])
# print(ingles_N)
# print(portugues_N)


palavras15 = """
Ordeal = provação
Ostrich = avestruz
Offset = deslocamento
Outboard = motor de popa
Outbreak = surto
Ornaments = enfeites
Outskirts = arredores
Owed = devido(a)
Ongoing = em progresso / em andamento / contínuo
Outdoor gatherings = encontros ao ar livre
Odd = ímpar / estranho / esquisito
Oughta = deveria
Ominous = sinistro(a)
Outrageous = ultrajante / escandaloso / chocante
Ordinary = comum / normal / ordinário
Owe = dever / estar em dívida / estar obrigado
Overcrowded = superlotado(a) / abarrotado / sobrecarregado
Overlook = negligenciar / omitir / deixar passar
Outdone = superado(a) / ultrapassar / exceder / sobrepujar
Op-ed = editorial
Otherwordly = sobrenatural / transcendental / alheio a este mundo
Overturned = derrubado(a)
Outline = contorno / esboço / perfil
Overturn = reviravolta
Outburst = explosão
Overwhelming = muito pesado / esmagador / opressivo
Obese = obeso 
Overjoyed = muito feliz
Overseas-registered = registrado no exterior
Open-pit = a céu aberto
Over time = com o tempo
Overshadowing = ofuscando
Off guard = desprevinido
Outright = sem rodeios / total / completo
Offshore = no mar / no alto mar
Outstanding = excepcional
Outnumbered = em menor número
Offender = delinquente / ofensor(a)
Overshadowed = ofuscado(a)
"""

linhas15 = palavras15.strip().split('\n')
# print(linhas15)

ingles_O = []
portugues_O = []

for linha in linhas15:
    ingles_O.append(linha.split(' = ')[0])
    portugues_O.append(linha.split(' = ')[1])
# print(ingles_O)
# print(portugues_O)


palavras16 = """
Police constable = agente de polícia
Pours = derrama
Portrayal = retrato
Polls = enquetes
Price gouging = manipulação de preços
Postponed = adiado(a)
Pristine = imaculado(a)
Packaging = embalagem
Praised = elogiado(a)
Poultry = aves
Playfully  = divertidamente
Pale = pálido
Poaching = caça furtiva
Pursue / Pursuit = perseguir
Pawn = penhor
Peril / danger = perigo
Peel = casca
Patch = correção / remendo
Punch through = perfurar
Plumbing = encanamento
Paycheck = contracheque
Pennies = moedas de um centavo
Physicians = médicos(as)
Pence = centavo
Prosecutors = procuradoras(es)
Poppy = papoula
Pod = vagem / o casulo
Party = festa / o partido
Pass out = desmaiar
Psyched = empolgado(a)
Pricey delicacy = iguaria cara
Perceive = compreender / perceber / entender
Panting / gasping = ofegante
Pounding = batendo
Purring = ronronar
Prejudiced = preconceituoso(a)
Plastic-wrapped = embrulhado em plástico
Posthumous = póstumo(a)
Peek = olhadinha / espreitar / espiar
Pliante = flexível
Prat = idiota
Pinpoint = identificar / apontar / localizar com precisão
Pole = poste / mastro
Puzzled = intrigado(a)
Premises = instalações
Prone = propenso(a)
Power disruption = interrupção de energia
Pipelines = oleodutos
Phasing out = eliminando gradualmente
Portly = corpulento(a)
Peak = pico / auge / cume / bico
Prevalent = predominante
Portraits = retrato
Proctor = inspetor
Piglets = leitões / leitoas
Prior = prévio(a) / anterior / antecedente
Parry = desviar-se / desviar / evitar / parar
Pouring = derramando 
Prioritizing = priorizando
Pottery = cerâmica
Pinkie = dedo mindinho
Payment voucher = comprovante de pagamento
Peacekeeping = manutenção da paz
Peanuts = amendoim
Pageant = concurso
Perished = pereceu / morrer / deixar de existir
Perch = poleiro
Perched = empoleirado(a)
Preschoolers = pré-escolares
Painstakingly = meticulosamente
Pranksters = brincalhões
Profit = lucro / proveito / benefício
Pull = puxar
Push = empurrar
Postpone = adiar
Placement test = teste de nivelamento
"""

linhas16 = palavras16.strip().split('\n')
# print(linhas16)

ingles_P = []
portugues_P = []

for linha in linhas16:
    ingles_P.append(linha.split(' = ')[0])
    portugues_P.append(linha.split(' = ')[1])
# print(ingles_P)
# print(portugues_P)


palavras17 = """
Quarreled = brigou / discutir / disputar
Quotes = citações 
Quagmire = atoleiro / pântano / lamaçal
Quake / earthquake = terremoto
Qualify = qualificar / calssificar / beneficiar
Quarantine = quarentena
Queue = fila
Quitter = desistente / molenga / perdedor
Quiver = tremor
Quote = citar / cotar / indicar
Quickened = acelerou
"""

linhas17 = palavras17.strip().split('\n')
# print(linhas17)

ingles_Q = []
portugues_Q = []

for linha in linhas17:
    ingles_Q.append(linha.split(' = ')[0])
    portugues_Q.append(linha.split(' = ')[1])
# print(ingles_Q)
# print(portugues_Q)

palavras18 = """
Rattlesnakes = cascavéis
Rattles = chocalhos
Reasoning = raciocínio
Rainforest = floresta tropical
Rents = aluguéis
Roughly = aproximadamente
Ribs = costela
Relies = confia
Rows = linhas
Rowing = remo
Rinks = pistas
Reemerged = ressurgiu
Reportedly = supostamente / alegadamente
Reinstated = restabelecido(a) 
Row = fila
Raw / rare = cru / crua
Rubbish = bobagem / entulho
Relentless = implacável
Recidivism = reicidência
Reassignment = reatribuição
Rate = avaliar
Reliability = confiabilidade
Ripen = amadurecer
Rumbling = estrondoso(a)
Reckon = contar
Round up = arredondar para cima
Ragged = esfarrapado
Roofs = telhados
Rusty = oxidada(o)
Rugged = áspero(a)
Riot = tumulto
River bank = margem do rio
Railway = estrada de ferro / ferrovia
Reassured = tranquilizado(a)
Robes = vestes
Rushed = apressado(a)
Remarks = observações
Reconcile = conciliar
Robbery = roubo
Rim = aro
Racoon = guaxinim
Regard = considerar / respeitar
Rod = haste / cajado / vara
Rat = ratazana
Regarding = em relação a / a respeito de / relativamente a
Resemble = assemelhar
Rip = rasgar
Regrettably = lamentavelmente
Ranged = variado(a)
Retrieval = recuperação / o restabelecimento / a reaquisição
Rough = duro / áspero / rude / agitado
Retailers = revendedores(as)
Riled = irritado(a)
Rely = contar com / depender
Regrettable = lamentável / deplorável / lastimável
Reckons = calcula / considera
Remarkably = notavelmente / extraordinariamente / invulgarmente
Relief = alívio / relevo
Rotten = podre
Rendezvous = encontro
Rattled = abalado(a)
Rucksack = mochila
Raggedly = irregularmente
Relish = saborear / apreciar
Rebounded = recuperou / repercurtir / ressaltar / ricochetear / ressoar
Roundabout = desvio
Realm = reino / domínio / esfera
Request = pedido
Rejoice = alegrar
Ran a business = administrou um negócio
Regardless = sem considerar / indiferente / descuidado / desatento
Runoff = escoamento
Rearrange = reorganizar / rearranjar
Ranged = variado(a)
Range = alcance
Reconnaissance = reconhecimento / verificação / exploração
Razorblade = lâmina de barbear / gilete
Ruthless = impiedoso(a)
Rag = trapo / farrapo / lenço
Ridges = cumes
Renewable = renovável
Rash = irritação na pele / erupção cutânea / assadura
Ruckus = tumulto
Rekindles = reacende
Reinsurance = resseguro
Run = gerenciar / realizar / correr
Rubble = destroços / pedregulho
Rush = correr / apressar / invadir
Riverbed = leito do rio / fluvial
Resume / curriculum = currículo
Riverside = beira do rio / margem do rio / ribeira
Retail = retalho / varejo
Renowned = renomado(a)
Reliable = confiável
Ripped out = arrancado
Rhombus = Losango
Rioters = manifestantes
Regret over = lamentar sobre
Remnants = restos
Ravine = ravina / barranco / desfiladeiro
"""

linhas18 = palavras18.strip().split('\n')
# print(linhas18)

ingles_R = []
portugues_R = []

for linha in linhas18:
    ingles_R.append(linha.split(' = ')[0])
    portugues_R.append(linha.split(' = ')[1])
# print(ingles_R)
# print(portugues_R)


palavras19 = """
Shortages = escassez 
Scarcity = escassez
Soared = subiu
Survey = pesquisa
Shorelines = costas
Stinger devices = dispositivos de ferrão
Span = período
Sparked = provocou
Subtle flaws = falhas sutis
Spread = propagação
Shepherd = pastor(a)
Stubbornness = teimosia
Specks = manchas
Southwestern = sudoeste
Sharp = afiado(a)
Swept = varrido(a)
Spokesperson = porta-voz
Shaken = abalado(a)
Stranded = encalhada(o) / abandonado(a) / sem recursos
Showcasing = apresentando
Seized = apreendido(a)
Strict = rigoroso(a)
Standstill = paralisação
Stuck = grudou
Stuffed = recheado(a)
Souvenirs = recordações
Scarce = escasso(a)
Scalpers = cambistas
Sample = amostra
Swirl = redemoinho
Spotted = identificado(a) / manchado
Soft drinks = refrigerante
Smearing = manchando
Strains = deformação
Sprinting = correndo
Stood = ficou
Shelter = abrigo
Site = local
Stripping off = arrancar
Savvy = experiente / conhecedor
Surgery = cirurgia
Similar = semelhante
Store = armazenar
Stock = estoque
Slightly = levemente
Shelling = bombardeio
Sewer = esgoto
Smirking = sorrindo maliciosamente
Scarcely = dificilmente
Sacking = despedindo
Shriveled = enrugado(a)
Steady = estável
Sink = pia / afundar
Spin = rodar
Spins = rotaciona
Shipments = remessos(as)
Smuggled = contrabandeado(a)
Sprawling = extenso(a)
Strap = alça
Standard = padrão
Sank = afundou
Shipwrecks = naufrágios
So on = assim por diante
Suitable = adequada(o)
Sap = seiva
Sloth = bicho-preguiça
Sheriff’s deputy = vice do xerife
Sudden = de repente
Spotlight = holofote
Stray bullet = bala perdida
Slay = arrasar
Stuttering = engasgando
Slopes = encostas
Source = fonte
Spoil = estragar
Sleeve = manga(camisa)
Shallow = raso(a) / superficial
Superficial = superficial
Storey = andar
Soak = absorver / encharcar
Scramble = passeio / subida / atropelo
Sigh = suspirar
Spit = cuspir
Stumble = tropeçar
Swallow = engolir
Schedule = agendar / programar / planejar / escalar / cronograma
Sobbing = soluçando
Skulking = escondido(a)
Sweaty = suado
Seedlings = mudas
Spooky = assustador(a)
slaughtered = abatido(a)
slaughterer = abatedor(ra)
Stew = ensopado(a)
Shortage = falta
Sworn in = empossado(a)
Skeptic = cético
Slang = gíria
Slung = pendurado(a)
Sidewalk = calçada
Shuttle = transporte
Stood up = levantou
Scalp = couro cabeludo
Snout = focinho
Squeals = gritos
Sin = pecado
Strongholds = fortaleza
Shareholder = acionista
Split = dividir
Sticking = colando
Stroke = acidente vascular cerebral / o golpe / a apoplexia / a pancanda
Squeezes = aperta 
Stricter = mais rigoroso
Sever = cortar / romper / separar
Sideways = lateralmente / de lado
Sledgehammers = marretas
Suitor = pretendente
Seafood = frutos do mar
Semiannual / biannual = semestral
Strikingly = surpreendentemente
Squeaking = rangendo
Scum = escumalha / espuma / escória
Strove = esforçou-se
Slither = deslizar
Sobering = sóbrio(a)
Spearmint = hortelã
Snogging = beijando
Sniffling = fungando
Smuggles = contrabandeado
Stance = posição / postura
Scatter = espalhar / dispersar / disseminar
Stretches  = alongar / se estende
Surroundings = arredores / ambiente 
Scenic = cênico(a) / pitoresco / teatral
Summit = cume / cúpula
Suppers = ceia / jantar
Softly = suavemente
Stammers = gagueja
Snitch = dedo duro
Speaking of which = falando nisso
Shovel = pá
Slaughterer = abatedor(a)
Staple food = alimento básico
Stubborn = teimoso(a) / obstinado
Slandered = caluniado(a)
Sewed = costurou
Seasoning = tempero
Spicy = apimentado / picante
Seemingly = aparentemente
Setting = contexto
Skyward bound = rumo ao céu
Speaker = caixa de som / alto-falante / orador / palestrante
Stretch = esticar
Stumbled = tropeçou
Stacks = empilha
Steadfast = firme / constante / inabalável / estável
Slate = lousa / quadro-negro / ardósia
Slippery = escorregadio(a)
Shrewd = astuto(a) / sagaz / perspicaz
Steam = vapor
Subtle = sútil
Scabbards = bainhas
Shaves his head = raspa a cabeça
Stencilling = estêncil
Scorching = abrasador(a) / ardente
Swift = veloz
Scalpel = bisturi
Stocks = ações 
Spiked = cravado(a)
Shipser = Navio
Sweltering = sufocante / abafa / sufoca de calor
Starving = morrendo de fome
Stingy = mesquinho
Spotless = impecável / limpo
Sorrowful = triste / doloroso / cheio de pena
Serene = serena / calmo / sossegado
Slovenly = sujo / mal vestido / desleixado
Soaked = ensopado
Sluggish = lerdo / lento
Swamped = inundados
Surrounding = em torno da / ambiente
Swathes = faixas / trigos
Sightings = avistamentos
Sewing = de costura / para costurar
Scoreboard = placar
Suing = processando
Silly = bobo(a)
Scales = balança / escamas
Smallpox = varíola
Spurred = estimulado(a)
Shaft = haste
Secuity issue = questão de segurança
Sprained = torcido(a)
Steaming = vapor
Spitting = cuspir
Surfaced = à tona
Sauce = molho
Spout / tap = bica
Sow = semear
Smeared = manchado(a)
Snapshot = instantâneo(a)
Shrinking = encolhendo
Shedding = derramamento
Shipping = envio / expedição / remessa
Skill-set = conjunto de habilidades
Scope = alcance / escopo
Shot up = disparou
Skilled = especializado(a) / hábil / perito
Sought = procurado(a) / solicitado
Stocking up = estocando
Snorkels = tubo respiratório para mergulho
Stick = grudar / vara / pau
Smugglers = contrabandistas
Shore = costa / praia / margem
Sheet / bed sheet = lençol
Supply chain = cadeia de mantimentos / suprimento
Squats / Squatting  = agachamentos
Swell = inchar
Skinny jeans = calça justa
Swelling = inchaço
Slim = afinar
Swan = nadou
Swum = nadado(a)
Surrounded = cercado
Spokesman / spokeswoman / spokesperson = porta-voz
Strike = ataque / greve
Sachets = sachês
Smuggle = contrabandear
Strive = esforço
Secedes = separa
Stormed = invadiram
"""

linhas19 = palavras19.strip().split('\n')
# print(linhas19)

ingles_S = []
portugues_S = []

for linha in linhas19:
    ingles_S.append(linha.split(' = ')[0])
    portugues_S.append(linha.split(' = ')[1])
# print(ingles_S)
# print(portugues_S)


palavras20 = """
Tonnes = toneladas
Trolley = carrinho
Triggered = provocado(a)
Tides = marés
Threatened = ameaçado(a)
Trawlers = arrastões
Taint = manchar
Turkeys = perus
Trapped = encurralada(o)
Thin = afinar
Tempt = tentada(o)
Taxpayers = contribuintes
Thorough = minucioso(a)
Tough = difícil
Taught = ensinou
Though = apesar / embora / entretanto
Thought = pensei
Through = através
Throughout = ao longo
Thus = portanto / assim / deste modo
Tusks = presas
Ticket gate = bilheteria / catraca
Tow or Tug = reboque
Tap water = água da torneira
Takes off = decola
Timber = madeira
To reconcile = reconciliar
Thumbs = polegares
Trap door = alçapão
Torso = tronco
Thigh = coxa
Tuck in = aconchegue-se
Tatty = esfarrapado
Tampered = adulterado(a)
Tough-talking = durão
Tumble = cair / a queda
Took hold = tomou conta
Tend = tratar / guardar / cuidar de
Tightened = apertado(a) / cerrar / esticar
Teargas = gás lacrimogêneo
Toughness = dureza
Trite = trivial / banal
Tiresome = cansativo(a)
Tilt = inclinar / pender / virar
Tap = toque / bica / torneira
Teensy = pequenino(a)
Thievery = roubo / furto
Tryouts = testes
Tusk = presa
Therefore = portanto
Torn = rasgado(a) / despedaçado
Trek = caminhada / viagem
Tent = barraca / tenda
Treacherous = traiçoeiro(a)
Thrice = três vezes
That went well = correu bem
Throw off = jogar fora
Throwing away = jogando fora
Threw away = jogou fora
Tug of war = cabo-de-guerra
Threw = jogou
Takeover = assumir
Training facility = instalação de treinamento
Twisting = torcendo / torção
Tighten = aperte
Tuning = afinação
Thrilled = emocionado
Terrific = fantástico
Tedious = tedioso
Towering = elevando-se / altaneiro / muito elevado
Tiny = muito pequeno
Telltale = revelador
Take a bow = curve-se
Take down = derrubar
Transfer voucher = comprovante de transferência
Torn down = demolido
Tiles = azulejos / telha
Trendy = na moda / última moda
Tingly = dormentes
Tributaries = afluentes
Toll = pedágio
Topped = coberto(a)
Towed = rebocado(a)
Tooth decay = cárie dentária
Trams = bondes
"""

linhas20 = palavras20.strip().split('\n')
# print(linhas20)

ingles_T = []
portugues_T = []

for linha in linhas20:
    ingles_T.append(linha.split(' = ')[0])
    portugues_T.append(linha.split(' = ')[1])
# print(ingles_T)
# print(portugues_T)


palavras21 = """
Under threat = sob ameaça
Underneath = por baixo
Upsurge = surto
Unassisted = sem ajuda / assistência
Upend = derrubar
Uninjured = ileso(a)
Unmanageable = ingovernável
Unflushable = impenetrável
Undercount = subconta
Unwillingly = a contragosto
Underage = menor de idade
Unfold = desdobrar / revelar
Unwillingness = falta de vontade / relutância
Unborn = por nascer / ainda não nascido / futuro
Unique = exclusivo(a) / único / sem igual
Unhinge = desequilibrar / pertubar / transtornar / desengonçar
Unpleasant = desagradável / aborrecido / antipático
Understandable = compreensível
Upholstery = estofamento
Uneasy = inquieto(a) / apreensivo / preocupado
Unyielding = inflexível
Unfailingly = infalivelmente
Utter = total / absoluto / completo
Uttered = pronunciou / proferir / dizer
Undergo = submeter-se a 
Understandably = compreensível
Unveiled = revelado(a)
Unemployment = desemprego
Unpredictable = imprevisto / imprevisível
Undercover = disfarçado(a)
Unchained = desencadeado(a)
Unconscious = inconsciente / desmaiado / sem sentidos
Uniquely = unicamente
Underway = em andamento
Unwanted = indesejado(a)
Unmitigated = absoluto(a)
Urged = incitado(a)
Underwent = sofrer / passar por
Unfolded = desdobrado(a)
Upended = de cabeça para baixo
Undid = desfez / desatar / soltar
Undergo = submeter-se a / sofrer / passar por
Unaided = sem ajuda
Unseats = destitui
Unsuspecting = desavisados
"""

linhas21 = palavras21.strip().split('\n')
# print(linhas21)

ingles_U = []
portugues_U = []

for linha in linhas21:
    ingles_U.append(linha.split(' = ')[0])
    portugues_U.append(linha.split(' = ')[1])
# print(ingles_U)
# print(portugues_U)


palavras22 = """
Venues = Locais
Vest = colete
Vacuum cleaner = aspirador de pó
Vault = cofre
Vow = juramento / o voto / a promessa
Vessel = navio / receptáculo
Vendors = vendedores(as)
Vial = frasco(a)
Vegetarian = vegetariano
Vanishing = fuga / que desaparece / sumido
Veered = desviou
Visually impaired = deficiente visual
Verge = beira
"""

linhas22 = palavras22.strip().split('\n')
# print(linhas22)

ingles_V = []
portugues_V = []

for linha in linhas22:
    ingles_V.append(linha.split(' = ')[0])
    portugues_V.append(linha.split(' = ')[1])
# print(ingles_V)
# print(portugues_V)


palavras23 = """
Wheat = trigo
Ways to cope with stress = maneiras de lidar com o estresse
Wide net = rede larga
Wither = murchar
Was stuck = estava preso / estava grudado
Workload = carga de trabalho
Well-paid = bem remunerado
Wall display = exibição de parede
Wide = amplo(a)
Windshield wipers = limpadores de pára-brisa
Waste packaging = embalagens de lixo
Willing = disposto(a)
Wandered = vagueou
Wholeness = integridade
Wet wipes = lenços umidecidos
Whistling = assobio
Workload = carga de trabalho
Worship = adoração
Whimpering = choramingando 
Whooshing = assobiando
Whatsoever = de jeito nenhum
Wooden debris = detritros de madeira
Wreckage = destroços
Ward = enfermaria
Width = largura
Wildlife park = parque de vida selvagem
Wildlife authority = autoridade da vida selvagem
Wire = arame
Wits = juízo
Windowsill = peitoril da janela
Wirtchcraft = feitiçaria
Willow tree = salgueiro
Whilst in = enquanto em
Wardrobe = guarda-roupa
Willingly = de boa vontade
Welfare = bem-estar
Weighs = pesa
Wages = remunerações / salários
Wearisome = cansativo(a)
Wails = lamentos / chorar / gemer / prantear
Whereabouts = paradeiro
Wavelengths = comprimento de ondas
Western = ocidente
Wagging = abanando / sacudir
Wields = empunha / manejar / brandir
weaned = desmamado(a) / desabituar / afastar
Whopping = enorme / colossal / gritante
Would drag too much = arrastaria muito
Wife-to-be = futura esposa
Whipping = chicotear / surra
Warped = deformado(a)
Wander = perambular
Whilst = enquanto / embora
Wondrous to behold = maravilhoso de se ver
Wrapping factory = fábrica de embalagens
Writhing = contorcendo-se
Waitress = garçonete
Whether = se / ou / quer
Wound = ferimento / ferida
Wailing = lamentando
Worthwhile = que vale a pena
Within = dentro de
Wounded = ferido(a)
Wheelchairs = cadeiras de rodas
Widely = largamente
 Windshield = parabrisa
Windows-sill = peitoril da janela
Wicked = malvado(a) / cruel / imoral / perverso
Wispy whiskers = bigodes finos
Went bankrupt = foi à falência
Wrap = enrolar / envolver / cobrir
Wealthy = rico / endinheirado / próspero(a)
Write off = eliminar / reduzir / descartar
Wholesome = saudável
Worshippers = adoradores(as)
Within = dentro de
Wider = mais largo
Wacky = maluco(a) / excêntrico
Wig = peruca
Wettest = mais úmido
Weighted boulder = pedregulho pesado
Waists = cinturas
Waist-high = na altura da cintura
Whosever = quem quer que seja
Walkout = ir embora
Wary = cauteloso(a)
Weightlifter = levantador de peso
Watchful = vigilante
Weighing = pesagem
"""

linhas23 = palavras23.strip().split('\n')
# print(linhas23)

ingles_W = []
portugues_W = []

for linha in linhas23:
    ingles_W.append(linha.split(' = ')[0])
    portugues_W.append(linha.split(' = ')[1])
# print(ingles_W)
# print(portugues_W)


palavras24 = """
Xylophone = Xilofone
XL (extra large) = GG / grande
Xmas (Christmas) = natal
Xenial = hospitaleiro(a) / acolhedor
"""

linhas24 = palavras24.strip().split('\n')
# print(linhas24)

ingles_X = []
portugues_X = []

for linha in linhas24:
    ingles_X.append(linha.split(' = ')[0])
    portugues_X.append(linha.split(' = ')[1])
# print(ingles_X)
# print(portugues_X)


palavras25 = """
Year-round = durante todo o ano
Yacht = iate
Yam = bocejar
"""

linhas25 = palavras25.strip().split('\n')
# print(linhas25)

ingles_Y = []
portugues_Y = []

for linha in linhas25:
    ingles_Y.append(linha.split(' = ')[0])
    portugues_Y.append(linha.split(' = ')[1])
# print(ingles_Y)
# print(portugues_Y)


palavras26 = """
Zookeepers = tratadores(as)
Zapped = eletrocutado(a)
Zealot = fanático(a)
Zealous = zeloso(a) / fervoroso / dedicado
Zebra crossing = faixa de pedestre / faixa / passadeira
Zenith = auge / apogeu
Zest = entusiasmo / gosto
Zigzag = ziguezague
Zucchini = abobrinha
Zip lines = tirolesa
"""

linhas26 = palavras26.strip().split('\n')
# print(linhas26)

ingles_Z = []
portugues_Z = []

for linha in linhas26:
    ingles_Z.append(linha.split(' = ')[0])
    portugues_Z.append(linha.split(' = ')[1])
# print(ingles_Z)
# print(portugues_Z)
