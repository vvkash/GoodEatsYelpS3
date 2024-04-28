const { Client, IntentsBitField} = require('discord.js');

const mainClient = new Client({
    intents: [
        IntentsBitField.Flags.Guilds,
        IntentsBitField.Flags.GuildMembers,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.MessageContent,
    ],
});

Client.login(
    'MTEzMjgwMzU1NjM3ODkzNTM4Nw.GKhHDH.Uls5vGF_jKV2gvs-0y5aKVbtavMiD8b3y59t6c'
);