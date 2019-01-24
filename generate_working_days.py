import click
import calendar
import pandas as pd

from datetime import date

from workalendar import europe, america, asia, oceania, africa


instances = {
    'Algeria': africa.Algeria(),
    'Angola': africa.Angola(),
    'Benin': africa.Benin(),
    'IvoryCoast': africa.IvoryCoast(),
    'Madagascar': africa.Madagascar(),
    'SaoTomeAndPrincipe': africa.SaoTomeAndPrincipe(),
    'SouthAfrica': africa.SouthAfrica(),
    'Alberta': america.Alberta(),
    'Brazil': america.Brazil(),
    'BrazilAcre': america.BrazilAcre(),
    'BrazilAlagoas': america.BrazilAlagoas(),
    'BrazilAmapa': america.BrazilAmapa(),
    'BrazilAmazonas': america.BrazilAmazonas(),
    'BrazilBahia': america.BrazilBahia(),
    'BrazilBankCalendar': america.BrazilBankCalendar(),
    'BrazilCariacicaCity': america.BrazilCariacicaCity(),
    'BrazilCeara': america.BrazilCeara(),
    'BrazilDistritoFederal': america.BrazilDistritoFederal(),
    'BrazilEspiritoSanto': america.BrazilEspiritoSanto(),
    'BrazilGoias': america.BrazilGoias(),
    'BrazilGuarapariCity': america.BrazilGuarapariCity(),
    'BrazilMaranhao': america.BrazilMaranhao(),
    'BrazilMatoGrosso': america.BrazilMatoGrosso(),
    'BrazilMatoGrossoDoSul': america.BrazilMatoGrossoDoSul(),
    'BrazilPara': america.BrazilPara(),
    'BrazilParaiba': america.BrazilParaiba(),
    'BrazilPernambuco': america.BrazilPernambuco(),
    'BrazilPiaui': america.BrazilPiaui(),
    'BrazilRioDeJaneiro': america.BrazilRioDeJaneiro(),
    'BrazilRioGrandeDoNorte': america.BrazilRioGrandeDoNorte(),
    'BrazilRioGrandeDoSul': america.BrazilRioGrandeDoSul(),
    'BrazilRondonia': america.BrazilRondonia(),
    'BrazilRoraima': america.BrazilRoraima(),
    'BrazilSantaCatarina': america.BrazilSantaCatarina(),
    'BrazilSaoPauloCity': america.BrazilSaoPauloCity(),
    'BrazilSaoPauloState': america.BrazilSaoPauloState(),
    'BrazilSergipe': america.BrazilSergipe(),
    'BrazilSerraCity': america.BrazilSerraCity(),
    'BrazilTocantins': america.BrazilTocantins(),
    'BrazilVilaVelhaCity': america.BrazilVilaVelhaCity(),
    'BrazilVitoriaCity': america.BrazilVitoriaCity(),
    'BritishColumbia': america.BritishColumbia(),
    'Canada': america.Canada(),
    'Chile': america.Chile(),
    'Colombia': america.Colombia(),
    'Manitoba': america.Manitoba(),
    'Mexico': america.Mexico(),
    'NewBrunswick': america.NewBrunswick(),
    'Newfoundland': america.Newfoundland(),
    'NorthwestTerritories': america.NorthwestTerritories(),
    'NovaScotia': america.NovaScotia(),
    'Nunavut': america.Nunavut(),
    'Ontario': america.Ontario(),
    'Panama': america.Panama(),
    'PrinceEdwardIsland': america.PrinceEdwardIsland(),
    'Quebec': america.Quebec(),
    'Saskatchewan': america.Saskatchewan(),
    'Yukon': america.Yukon(),
    'HongKong': asia.HongKong(),
    'Japan': asia.Japan(),
    'Malaysia': asia.Malaysia(),
    'Qatar': asia.Qatar(),
    'Singapore': asia.Singapore(),
    'SouthKorea': asia.SouthKorea(),
    'Taiwan': asia.Taiwan(),
    'Austria': europe.Austria(),
    'BadenWurttemberg': europe.BadenWurttemberg(),
    'Bavaria': europe.Bavaria(),
    'Belgium': europe.Belgium(),
    'Berlin': europe.Berlin(),
    'Brandenburg': europe.Brandenburg(),
    'Bremen': europe.Bremen(),
    'Bulgaria': europe.Bulgaria(),
    'Catalonia': europe.Catalonia(),
    'Croatia': europe.Croatia(),
    'Cyprus': europe.Cyprus(),
    'CzechRepublic': europe.CzechRepublic(),
    'Denmark': europe.Denmark(),
    'Estonia': europe.Estonia(),
    'EuropeanCentralBank': europe.EuropeanCentralBank(),
    'Finland': europe.Finland(),
    'France': europe.France(),
    'FranceAlsaceMoselle': europe.FranceAlsaceMoselle(),
    'Germany': europe.Germany(),
    'Greece': europe.Greece(),
    'Hamburg': europe.Hamburg(),
    'Hesse': europe.Hesse(),
    'Hungary': europe.Hungary(),
    'Iceland': europe.Iceland(),
    'Ireland': europe.Ireland(),
    'Italy': europe.Italy(),
    'Latvia': europe.Latvia(),
    'Lithuania': europe.Lithuania(),
    'LowerSaxony': europe.LowerSaxony(),
    'Luxembourg': europe.Luxembourg(),
    'Malta': europe.Malta(),
    'MecklenburgVorpommern': europe.MecklenburgVorpommern(),
    'Netherlands': europe.Netherlands(),
    'NorthRhineWestphalia': europe.NorthRhineWestphalia(),
    'Norway': europe.Norway(),
    'Poland': europe.Poland(),
    'Portugal': europe.Portugal(),
    'RhinelandPalatinate': europe.RhinelandPalatinate(),
    'Romania': europe.Romania(),
    'Russia': europe.Russia(),
    'Saarland': europe.Saarland(),
    'Saxony': europe.Saxony(),
    'SaxonyAnhalt': europe.SaxonyAnhalt(),
    'SchleswigHolstein': europe.SchleswigHolstein(),
    'Slovakia': europe.Slovakia(),
    'Slovenia': europe.Slovenia(),
    'Spain': europe.Spain(),
    'Sweden': europe.Sweden(),
    'Switzerland': europe.Switzerland(),
    'Thuringia': europe.Thuringia(),
    'UnitedKingdom': europe.UnitedKingdom(),
    'UnitedKingdomNorthernIreland': europe.UnitedKingdomNorthernIreland(),
    'Vaud': europe.Vaud(),
    'Australia': oceania.Australia(),
    'AustralianCapitalTerritory': oceania.AustralianCapitalTerritory(),
    'Hobart': oceania.Hobart(),
    'MarshallIslands': oceania.MarshallIslands(),
    'NewSouthWales': oceania.NewSouthWales(),
    'NorthernTerritory': oceania.NorthernTerritory(),
    'Queensland': oceania.Queensland(),
    'SouthAustralia': oceania.SouthAustralia(),
    'Tasmania': oceania.Tasmania(),
    'Victoria': oceania.Victoria(),
    'WesternAustralia': oceania.WesternAustralia(),
}


african_countries = [country for country in dir(africa) if country[0].isupper()]
america_countries = [country for country in dir(america) if country[0].isupper()]
asian_countries = [country for country in dir(asia) if country[0].isupper()]
european_countries = [country for country in dir(europe) if country[0].isupper()]
oceania_countries = [country for country in dir(oceania) if country[0].isupper()]


country_mapping = {
    'africa': african_countries,
    'america': america_countries,
    'asia': asian_countries,
    'europe': european_countries,
    'oceania': oceania_countries
}


@click.command()
@click.argument('filename')
@click.option('--years', '-y', multiple=True, help='Required years (if void will generate 2008 to 2030).')
@click.option('--zones', '-z', multiple=True, help='Zone name in English [europe|africa|asia|america|oceania] (default: europe)')

def generate_workdays(zones, years, filename):
    working_days = [('country', 'year', 'month', 'workdays_nb')]
    if len(years) == 0:
        years = range(2008, 2031)
    if len(zones) == 0:
        zones = ['europe',]
    countries = []
    for zone in zones:
        countries += country_mapping[zone]
    for country in countries:
        try:
            cal = instances[country]
        except KeyError:
            print("Country {} is not available.".format(country))
        for year in years:
            year = int(year)
            for month in range(1, 13):
                min_day, max_day = calendar.monthrange(year, month)
                min_date = date(year, month, 1)
                max_date = date(year, month, max_day)
                working_days_nb = 0
                for day in range(1, max_day + 1):
                    if cal.is_working_day(date(year, month, day)) is True:
                        working_days_nb += 1
                working_days.append((country, year, month, working_days_nb))

    workdays_df = pd.DataFrame(working_days[1:], columns=working_days[0])
    workdays_df.to_excel(filename, index=False)

if __name__ == '__main__':
    generate_workdays()
