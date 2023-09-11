from telebot.asyncio_storage.base_storage import StateStorageBase, StateContext
import os

import pickle


class StatePickleStorage(StateStorageBase):
    def __init__(self, file_path="./.state-save/states.pkl") -> None:
        self.file_path = file_path
        self.create_dir()
        self.data = self.read()

    async def convert_old_to_new(self):
        new_data = {key: {key: value} for key, value in self.data.items()}
        # pass it to global data
        self.data = new_data
        self.update_data() # update data in file

    def create_dir(self):
        """
        Create directory .save-handlers.
        """
        dirs, filename = os.path.split(self.file_path)
        os.makedirs(dirs, exist_ok=True)
        if not os.path.isfile(self.file_path):
            with open(self.file_path,'wb') as file:
                pickle.dump({}, file)

    def read(self):
        with open(self.file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    
    def update_data(self):
        with open(self.file_path, 'wb+') as file:
            pickle.dump(self.data, file, protocol=pickle.HIGHEST_PROTOCOL)

    async def set_state(self, chat_id, user_id, state):
        if hasattr(state, 'name'):
            state = state.name
        if chat_id in self.data:
            if user_id in self.data[chat_id]:
                self.data[chat_id][user_id]['state'] = state
            else:
                self.data[chat_id][user_id] = {'state': state, 'data': {}}
            self.update_data()
            return True
        self.data[chat_id] = {user_id: {'state': state, 'data': {}}}
        self.update_data()
        return True
    
    async def delete_state(self, chat_id, user_id):
        if self.data.get(chat_id):
            if self.data[chat_id].get(user_id):
                del self.data[chat_id][user_id]
                if chat_id == user_id:
                    del self.data[chat_id]
                self.update_data()
                return True

        return False

    
    async def get_state(self, chat_id, user_id):
        if self.data.get(chat_id):
            if self.data[chat_id].get(user_id):
                return self.data[chat_id][user_id]['state']

        return None
    async def get_data(self, chat_id, user_id):
        if self.data.get(chat_id):
            if self.data[chat_id].get(user_id):
                return self.data[chat_id][user_id]['data']
        
        return None

    async def reset_data(self, chat_id, user_id):
        if self.data.get(chat_id):
            if self.data[chat_id].get(user_id):
                self.data[chat_id][user_id]['data'] = {}
                self.update_data()
                return True
        return False

    async def set_data(self, chat_id, user_id, key, value):
        if self.data.get(chat_id):
            if self.data[chat_id].get(user_id):
                self.data[chat_id][user_id]['data'][key] = value
                self.update_data()
                return True
        raise RuntimeError(f'chat_id {chat_id} and user_id {user_id} does not exist')

    def get_interactive_data(self, chat_id, user_id):
        return StateContext(self, chat_id, user_id)

    async def save(self, chat_id, user_id, data):
        self.data[chat_id][user_id]['data'] = data
        self.update_data()