'use strict';

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.createTable('techs', {
            id: {
                type: Sequelize.INTEGER,
                primaryKey: true,
                autoIncrement: true,
                allowNull: false,
            },
            name: {
                type: Sequelize.INTEGER,
                allowNull: false,
            },
            // eh soh automatizado pra ele preencher esses campos
            created_at: {
                type: Sequelize.DATE,
                allowNull: false
            },
            updated_at: {
                type: Sequelize.DATE,
                allowNull: false
            },

        });
    },

    down: (queryInterface, Sequelize) => {
        return queryInterface.dropTable('adresses');
    }
};