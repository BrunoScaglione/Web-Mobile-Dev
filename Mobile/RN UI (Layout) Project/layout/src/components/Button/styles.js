import {StyleSheet} from 'react-native';
import { metrics, colors, fonts } from '../../styles';

const styles = StyleSheet.create({
  // container de cada botao
  // essas propriedade sao em relacao ao texto
  container: {
    height: 31,
    backgroundColor: colors.primary,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: metrics.padding 
  },

  'button-outline' : {
    backgroundColor: colors.white,
    borderWidth: 1,
    borderColor: colors.primary
  },

  text: {
    color: colors.white,
    fontWeight: 'bold',
    fontSize: fonts.small,
  },

  'text-outline': {
    color: colors.primary,
    fontWeight: 'bold',
    fontSize: fonts.small,
  }

});

export default styles;