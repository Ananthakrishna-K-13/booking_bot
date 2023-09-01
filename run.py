from booking.booking import Booking

bot = Booking()
bot.land_first_page()
bot.changeCurrency()
bot.select_place_to_go("New York")
bot.select_dates(checkin="2023-09-04",checkout="2023-09-09")
bot.select_occupancy(7)
bot.click_search()
bot.apply_filtration()
bot.driver.refresh()
bot.report_results()