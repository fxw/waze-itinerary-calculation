import WazeRouteCalculator
import logging
logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

from_address = '44.7849451,-0.4747446' #'48.7813076,2.2353371'
to_address = '44.8609818,-0.5541567' #'48.8699547,2.4009557'
region = 'EU'
vehicle_type = 'MOTORCYCLE'

route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
route.calc_all_routes_info(time_delta=-480)