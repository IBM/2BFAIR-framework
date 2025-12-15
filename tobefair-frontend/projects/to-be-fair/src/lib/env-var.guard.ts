import {
  ActivatedRouteSnapshot,
  CanActivate,
  RouterStateSnapshot,
  UrlTree,
} from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { firstValueFrom, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class EnvVarGuard implements CanActivate {
  public backendUrl = '';

  constructor(private _httpClient: HttpClient) {
    // Empty.
  }

  canActivate(
    route: ActivatedRouteSnapshot,
    state_: RouterStateSnapshot,
  ):
    | Observable<boolean | UrlTree>
    | Promise<boolean | UrlTree>
    | boolean
    | UrlTree {
    const urlWithParams = `/get-backend`;

    return firstValueFrom(
      this._httpClient.get<string>(urlWithParams, {
        responseType: 'text' as 'json',
      }),
    )
      .then((value) => {
        console.log(value);
        this.backendUrl = value;
        return true;
      })
      .catch((err) => {
        console.error('Erro na requisição:', err);
        return true;
      });
  }
}
