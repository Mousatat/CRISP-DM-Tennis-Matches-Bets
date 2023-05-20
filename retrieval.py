import requests
import pandas as pd

API_BASE_URL = 'https://api.tipsscore.com'
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key


def get_player_info(player_id):
    url = f'{API_BASE_URL}/players/{player_id}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        player_data = response.json()
        player_info = {
            'player_id': player_data['player_id'],
            'full_name': player_data['full_name'],
            'last_name': player_data['last_name'],
            'Aces': player_data['Aces'],
            'Double Faults': player_data['Double Faults'],
            '1st Serve': player_data['1st Serve'],
            '1st Serve Points Won': player_data['1st Serve Points Won'],
            '2nd Serve Points Won': player_data['2nd Serve Points Won'],
            'Break Points Faced': player_data['Break Points Faced'],
            'Break Points Saved': player_data['Break Points Saved'],
            'Service Games Played': player_data['Service Games Played'],
            'Service Games Won': player_data['Service Games Won'],
            'Total Service Points Won': player_data['Total Service Points Won'],
            '1st Serve Return Points Won': player_data['1st Serve Return Points Won'],
            '2nd Serve Return Points Won': player_data['2nd Serve Return Points Won'],
            'Break Points Opportunities': player_data['Break Points Opportunities'],
            'Break Points Converted': player_data['Break Points Converted'],
            'Return Games Played': player_data['Return Games Played'],
            'Return Games Won': player_data['Return Games Won'],
            'Return Points Won': player_data['Return Points Won'],
            'Total Points Won': player_data['Total Points Won']
        }
        return player_info
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    player_ids = pd.read_csv('atp_players.csv')['player_id']  # Replace with the actual player ID
    df = pd.DataFrame()
    for player_id in player_ids:
        player_info = get_player_info(player_id)
        pi = pd.DataFrame(player_info)
        df = pd.concat([df, pi])

    df.to_csv('new_features.csv')


if __name__ == '__main__':
    main()
