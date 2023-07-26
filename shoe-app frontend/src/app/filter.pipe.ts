import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(arr: any[], prop: string, propScnd: string, propThird: string, value: string): any {
    if (arr) {
      if (!value) {
        return arr
      } else {
        return arr.filter(obj => this.filter(obj[prop], obj[propScnd], obj[propThird], value))
      }
    } else {
      return []
    }
  }

  filter(source: string, sourceScnd: string, sourceThird: string, target: string): boolean {
    return (source.toLowerCase().includes(target.toLowerCase()) || sourceScnd.toLowerCase().includes(target.toLowerCase()) || sourceThird.toLowerCase().includes(target.toLowerCase()));
  }

}